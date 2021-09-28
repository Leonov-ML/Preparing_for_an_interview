from stack_app import balance


def test_bracket_success_1():
    expected = balance.check_is_line_correct('(((([{}]))))')
    assert expected


def test_bracket_success_2():
    expected = balance.check_is_line_correct('[([])((([[[]]])))]{()}')
    assert expected


def test_bracket_success_3():
    expected = balance.check_is_line_correct('{{[()]}}')
    assert expected


def test_bracket_failed_1():
    expected = balance.check_is_line_correct('}}{')
    assert not expected


def test_bracket_failed_2():
    expected = balance.check_is_line_correct('{{[(])]}}')
    assert not expected


def test_bracket_failed_3():
    expected = balance.check_is_line_correct('[[{())}]')
    assert not expected
