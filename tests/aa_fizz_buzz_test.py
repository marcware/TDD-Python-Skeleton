from src.aa_fizz_buzz import calculate


def test_send_one_response_one():
    response = calculate(1)
    assert response == '1'


def test_send_two_response_two():
    response = calculate(2)
    assert response == '2'


def test_send_three_response_fizz():
    response = calculate(3)
    assert response == 'fizz'


def test_send_four_response_four():
    response = calculate(4)
    assert response == '4'


def test_send_five_response_buzz():
    response = calculate(5)
    assert response == 'buzz'


def test_send_five_response_buzz():
    response = calculate(6)
    assert response == 'fizz'


def test_send_seven_response_seven():
    response = calculate(7)
    assert response == '7'


def test_send_eight_response_eight():
    response = calculate(8)
    assert response == '8'


def test_send_nine_response_fizz():
    response = calculate(9)
    assert response == 'fizz'


def test_send_ten_response_buzz():
    response = calculate(10)
    assert response == 'buzz'


def test_send_twelve_response_buzz():
    response = calculate(12)
    assert response == 'fizz'


def test_send_fifteen_response_fizzbuzz():
    response = calculate(15)
    assert response == 'fizzbuzz'

def test_send_any_number_response_fizzbuzz():
    response = calculate(30)
    assert response == 'fizzbuzz'