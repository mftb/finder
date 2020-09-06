import unittest
from finder import Finder
from pytest import raises


class FinderLargeTests(unittest.TestCase):
    # basic tests

    def test_sanity_check(self):
        string_list = ['asd', 'asdd', 'fre', 'glk', 'lkm']
        finder = Finder(string_list)
        assert finder.find('sad') == ['asd']

    # corner case tests

    def test_not_found(self):
        large_list = [str(i) for i in range(0, 10)]
        finder = Finder(large_list)
        assert finder.find('a') == []

    def test_empty_constructor(self):
        finder = Finder([])
        assert finder.find('a') == []

    def test_bad_contructor_type(self):
        string_dict = {"asd": "asd", "asdd": "asdd"}
        with raises(TypeError):
            finder = Finder(string_dict)
            assert finder.find('sad') == ['asd']

    def test_bad_find_type_param(self):
        string_list = ['asd', 'asdd', 'fre', 'glk', 'lkm']
        with raises(TypeError):
            finder = Finder(string_list)
            assert finder.find(123) == ['asd']

    def test_bad_string2dict_type(self):
        with raises(TypeError):
            assert isinstance(Finder._string2dict(123), tuple)
