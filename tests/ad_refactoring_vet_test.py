from mamba import description, context, it, before, after, after_all, before_all
from expects import expect, equal

from src.ad_refactoring_vet import Note, Case, Diagnosis, DiseaseFilter

with description('Disease filter') as self:
    with before.each:
        note_public = Note(1, 'public')
        note_private = Note(2, 'private')

        cases = [
            Case(1, 'Chupito', 1, 'Calicivirus', [note_public], [note_private]),
            Case(2, 'Juliana', 2, 'Epilepsia', [note_public], []),
            Case(3, 'Dinwell', 3, 'Otitis', [note_public], [])
        ]
        diagnoses = [
            Diagnosis(1, 'Calicivirus', 'Vías Respiratorias Altas', 'Respiratorio', 'Virus', 'Gato'),
            Diagnosis(2, 'Epilepsia', 'Cerebro', 'Neurológico', 'Idiopatico', 'Perro, Gato'),
            Diagnosis(3, 'Otitis', 'Oídos', 'Auditivo', 'Bacteria', 'Perro, Gato '),
            Diagnosis(4, 'Blefaritis', 'Cabeza y cuello, Ojos',
                      'Sistema Tegumentario, Oftalmológico, Órganos de los sentidos', 'Inflamatorio', 'Perro, Gato'),
            Diagnosis(5, 'Moquillo Felino (Panleucopenia)', 'Abdomen', 'Digestivo, Sistema Inmune', 'Infeccioso',
                      'Gato'),
            Diagnosis(6, 'Cardiomiopatía', 'Tórax', 'Cardiovascular', 'Degenerativo,Hereditario', 'Perro, Gato'),
            Diagnosis(7, 'Accidente Cerebrovascular', 'Cabeza y cuello', 'Sistema nervioso, Cardiovascular',
                      'Degenerativo, Metabólico, Inflamatorio', 'Perro, Gato'),
            Diagnosis(8,
                      'Moquillo Canino',
                      'Tórax, Abdómen, Sistema Tegumentario, Cabeza y cuello, Ojos',
                      'Respiratorio, Digestivo, Tegumentario, Nervioso, Oftalmológico, Órganos de los Sentidos',
                      'Infeccioso',
                      'Perro')
        ]
        self.diseases_filter = DiseaseFilter(cases, diagnoses)

    with context('filters cases when several diagnosis filters are applied together'):
        with it('Diagnose es for case'):
            self.diseases_filter.add_filter('Cerebro')
            self.diseases_filter.add_filter('Vías Respiratorias Altas')

            result = self.diseases_filter.cases_filtered()

            expect(result[0].patient_name).to(equal('Juliana'))
            expect(result[1].patient_name).to(equal('Chupito'))
