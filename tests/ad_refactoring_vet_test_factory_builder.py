from mamba import description, context, it, before, after, after_all, before_all
from expects import expect, equal

from src.ad_refactoring_vet import Note, Case, Diagnosis, DiseaseFilter

A_FIRST_PATIENT_NAME = 'Chupito'
A_FIRST_PATIENT_ID = 1

A_SECOND_PATIENT_NAME = 'Juliana'
A_SECOND_PATIENT_ID = 2

A_THIRD_PATIENT_NAME = 'Dinwell'
A_THIRD_PATIENT_ID = 3


class DiseaseFilterBuilder:
    def __init__(self):
        self.cases = []
        self.diagnoses = []

    def with_case(self, patient_name, diagnose_id):
        note_public = Note(1, 'A_PUBLIC_NOTE')
        note_private = Note(2, 'A_PRIVATE_NOTE')
        case = Case(0, patient_name, diagnose_id, 'A_DIAGNOSE_NAME', note_public, note_private)
        self.cases.append(case)
        return self

    def with_diagnose(self, diagnose_id, location):
        diagnose = Diagnosis(diagnose_id, 'A_NAME', location, 'A_SYSTEM', 'A_ORIGIN', 'A_SPECIE')
        self.diagnoses.append(diagnose)
        return self

    def build(self):
        return DiseaseFilter(self.cases, self.diagnoses)


with description('Disease filter') as self:
    with before.each:
        self.diseases_filter = DiseaseFilterBuilder() \
            .with_case(A_FIRST_PATIENT_NAME, A_FIRST_PATIENT_ID) \
            .with_case(A_SECOND_PATIENT_NAME, A_SECOND_PATIENT_ID) \
            .with_case(A_THIRD_PATIENT_NAME, A_THIRD_PATIENT_ID) \
            .with_diagnose(1, 'Vías Respiratorias Altas') \
            .with_diagnose(2, 'Cerebro') \
            .with_diagnose(3, 'Oídos') \
            .build()

    with context('filters cases when several diagnosis filters are applied together'):
        with it('Diagnose es for case'):
            self.diseases_filter.add_filter('Cerebro')
            self.diseases_filter.add_filter('Vías Respiratorias Altas')

            result = self.diseases_filter.cases_filtered()

            expect(result[0].patient_name).to(equal(A_SECOND_PATIENT_NAME))
            expect(result[1].patient_name).to(equal(A_FIRST_PATIENT_NAME))



