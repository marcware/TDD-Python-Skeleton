class Note:
    def __init__(self, note_id: int, content: str):
        self.note_id = note_id
        self.content = content


class Case:
    def __init__(self, case_id: int, patient_name: str, diagnosis_id: int, diagnosis_name: str, public_notes: [Note],
                 private_notes: [Note]):
        self.case_id = case_id
        self.patient_name = patient_name
        self.diagnosis_id = diagnosis_id
        self.diagnosis_name = diagnosis_name
        self.public_notes = public_notes
        self.private_notes = private_notes


class Diagnosis:
    def __init__(self, diagnosis_id: int, name: str, location: str, system: str, origin: str, specie: str):
        self.diagnosis_id = diagnosis_id
        self.name = name
        self.location = location
        self.system = system
        self.origin = origin
        self.specie = specie


class DiseaseFilter:
    _filters = []
    _filtered_cases = []

    def __init__(self, cases_insert: list[Case], diagnoses_insert: list[Diagnosis]):
        self.cases = cases_insert
        self.diagnoses = diagnoses_insert

    def add_filter(self, location: str):
        self._filters.append(location)

    def cases_filtered(self) -> list[Case]:
        _diagnoses_filtered_list = []

        def diagnoses_filtered_by(location_search: str) -> Diagnosis:
            for d in self.diagnoses:
                if d.location == location_search:
                    return d

        def from_diagnosis_to_cases_filtered(d: Diagnosis) -> None:
            for c in self.cases:
                if c.diagnosis_id == d.diagnosis_id:
                    self._filtered_cases.append(c)

        for location in self._filters:
            _diagnoses_filtered_list.append(diagnoses_filtered_by(location))

        for diagnose in _diagnoses_filtered_list:
            from_diagnosis_to_cases_filtered(diagnose)

        return self._filtered_cases


if __name__ == '__main__':
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
        Diagnosis(5, 'Moquillo Felino (Panleucopenia)', 'Abdomen', 'Digestivo, Sistema Inmune', 'Infeccioso', 'Gato'),
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
    diseases_filter = DiseaseFilter(cases, diagnoses)
    diseases_filter.add_filter('Cerebro')
    diseases_filter.add_filter('Vías Respiratorias Altas')

    result = diseases_filter.cases_filtered()

    print(result[0].patient_name)
    print(result[1].patient_name)

