import re


class CamelCase:
    def convert_string(self, data_to_convert: str) -> str:
        regex = r"[-_ ]"
        data_capitalize = data_to_convert.title()
        return re.sub(regex, '', data_capitalize)


if __name__ == '__main__':
    camel_case = CamelCase()
    response = camel_case.convert_string('foo_bar')
