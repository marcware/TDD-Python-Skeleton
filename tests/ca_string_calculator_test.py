from abc import ABC

from doublex import Spy
from doublex_expects import have_been_called
from mamba import description, it
from expects import expect, equal

from src.ca_string_calculator import StringCalculator

with description('String Calculator'):
    with description('Send None or empty value'):
        with it('Send None value return 0'):
            calculator = StringCalculator()

            result = calculator.calculate(None)

            expect(result).to(equal(0))
        with it('Send empty value return 0'):
            calculator = StringCalculator()

            result = calculator.calculate('')

            expect(result).to(equal(0))
    with description('Send String value'):
        with it('Send str "1" value return int 1'):
            calculator = StringCalculator()

            result = calculator.calculate('1')

            expect(result).to(equal(1))

        with it('Send str "1,2" value return int 3'):
            calculator = StringCalculator()

            result = calculator.calculate('1,2')

            expect(result).to(equal(3))
    with description('does not increment the total in case of non numeric symbol'):
        with it('Send str "a" value return int 0'):
            calculator = StringCalculator()

            result = calculator.calculate('a')

            expect(result).to(equal(0))
        with it('Send str "1,a,2" value return int 3'):
            calculator = StringCalculator()

            result = calculator.calculate('1,a,2')

            expect(result).to(equal(3))

        with it('Send str "1a,2" value return int 2'):
            calculator = StringCalculator()

            result = calculator.calculate('1a,2')

            expect(result).to(equal(2))
    with description('sums all the numbers separated by custom separator'):
        with it('Send str "//#/3#2" value return int 5'):
            calculator = StringCalculator()

            result = calculator.calculate('a')

            expect(result).to(equal(0))
