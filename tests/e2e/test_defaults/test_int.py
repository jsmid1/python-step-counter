# from tests.e2e.utils import is_recorded


def test_int_add(setup_module):
    recorder, recoding = setup_module

    with recoding():
        pass
        # x = 5
        # x = x + 5

    assert False  # is_recorded(recorder, int, '__add__')
