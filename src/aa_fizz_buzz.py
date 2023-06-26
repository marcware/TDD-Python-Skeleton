FIZZ = 'fizz'
BUZZ = 'buzz'
FIZZBUZZ = 'fizzbuzz'


def calculate(number: int) -> str:
    if _is_divisible_by(number, 15):
        return FIZZBUZZ
    if _is_divisible_by(number, 5):
        return BUZZ
    if _is_divisible_by(number, 3):
        return FIZZ

    return str(number)


def _is_divisible_by(number: int, divisor: int) -> bool:
    return number % divisor == 0
