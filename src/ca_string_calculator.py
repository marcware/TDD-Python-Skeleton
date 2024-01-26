import re


class StringCalculator:
    REGEX_SUM_CARACTER = r"\/\/(.*?)\/"
    REGEX = r"^[A-Za-z][A-Za-z0-9]*$|^\d+[A-Za-z]\d*$"

    def calculate(self, string_values: str | None) -> int:
        if (string_values is None) or (string_values == ''):
            return 0

        info = re.match(self.REGEX, string_values)
        print(info[0])
        if info is None:
            list_resultante = string_values.split(',')
        else:
            list_resultante = info[1].split(info[0])

        total = 0
        for value in list_resultante:
            if bool(re.match(self.REGEX, value)):
                continue

            total = total + int(value)

        return total
