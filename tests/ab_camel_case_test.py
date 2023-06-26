from src.ab_camel_case import CamelCase


def test_send_empty_return_empty():
    camel_case = CamelCase()
    assert camel_case.convert_string('') == ''


def test_send_Foo_return_Foo():
    camel_case = CamelCase()
    assert camel_case.convert_string('Foo') == 'Foo'


def test_send_Foo_Bar_return_FooBar():
    camel_case = CamelCase()
    response = camel_case.convert_string('Foo Bar')
    assert response == 'FooBar'


def test_send_Foo_BarFoo_return_FooBar():
    camel_case = CamelCase()
    response = camel_case.convert_string('Foo_Bar-Foo')
    assert response == 'FooBarFoo'


def test_converts_the_first_character_of_one_word_to_uppercase():
    camel_case = CamelCase()
    response = camel_case.convert_string('foo')
    assert response == 'Foo'

def test_converts_the_first_character_of_each_word_to_uppercase():
    camel_case = CamelCase()
    response = camel_case.convert_string('foo_bar')
    assert response == 'FooBar'
