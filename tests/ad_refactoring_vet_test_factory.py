from mamba import description, context, it, before, after, after_all, before_all
from expects import expect, equal

from src.ad_refactoring_vet import Note, Case, Diagnosis, DiseaseFilter
A_FIRST_PATIENT_NAME = 'Chupito'
A_FIRST_PATIENT_ID = 1

A_SECOND_PATIENT_NAME = 'Juliana'
A_SECOND_PATIENT_ID = 2

A_THIRD_PATIENT_NAME = 'Dinwell'
A_THIRD_PATIENT_ID = 3


with description('Disease filter') as self:
    with before.each:
        self.cases = [
            self._create_case(A_FIRST_PATIENT_NAME, A_FIRST_PATIENT_ID),
            self._create_case(A_SECOND_PATIENT_NAME, A_SECOND_PATIENT_ID),
            self._create_case(A_THIRD_PATIENT_NAME, A_THIRD_PATIENT_ID),
        ]
        self.diagnoses = [
            self._create_diagnose(1, 'Vías Respiratorias Altas'),
            self._create_diagnose(2, 'Cerebro'),
            self._create_diagnose(3, 'Oídos'),
        ]

    with context('filters cases when several diagnosis filters are applied together'):
        with it('Diagnose es for case'):
            self.diseases_filter = DiseaseFilter(self.cases, self.diagnoses)
            self.diseases_filter.add_filter('Cerebro')
            self.diseases_filter.add_filter('Vías Respiratorias Altas')

            result = self.diseases_filter.cases_filtered()

            expect(result[0].patient_name).to(equal(A_SECOND_PATIENT_NAME))
            expect(result[1].patient_name).to(equal(A_FIRST_PATIENT_NAME))


    def _create_diagnose(self, diagnose_id: int, location: str) -> Diagnosis:
        return Diagnosis(diagnose_id, 'A_NAME', location, 'A_SYSTEM', 'A_ORIGIN', 'A_SPECIE')


    def _create_case(self, patient_name: str, diagnose_id: int):
        note_public = Note(1, 'A_PUBLIC_NOTE')
        note_private = Note(2, 'A_PRIVATE_NOTE')
        return Case(0, patient_name, diagnose_id, 'A_DIAGNOSE_NAME', note_public, note_private)
