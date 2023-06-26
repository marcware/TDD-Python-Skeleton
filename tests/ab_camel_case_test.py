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
