import unittest
from finder import Finder
from pytest import raises


class FinderTests(unittest.TestCase):
    # basic tests
    def test_sanity_check(self):
        string_list = ['asd', 'asdd', 'fre', 'glk', 'lkm']
        finder = Finder(string_list)
        assert finder.find('sad') == ['asd']

    # large tests

    def test_large_constructor_list(self):
        large_list = ['abc' for i in range(0,1000000)]
        finder = Finder(large_list)
        assert finder.find('abc') == large_list

    def test_large_haystack_single_needle(self):
        large_list = [str(i) for i in range(0,1000000)]
        finder = Finder(large_list)
        assert finder.find('123') == ['123', '132', '213', '231', '312', '321']

    # corner case tests

    def test_not_found(self):
        large_list = [str(i) for i in range(0,1000000)]
        finder = Finder(large_list)
        assert finder.find('a') == []

    def test_empty_constructor(self):
        finder = Finder([])
        assert finder.find('a') == []

    def test_bad_contructor_type(self):
        string_dict = {"asd":"asd", "asdd":"asdd"}
        with raises(TypeError):
            finder = Finder(string_dict)
            assert finder.find('sad') == ['asd']

    def test_bad_find_type_param(self):
        string_list = ['asd', 'asdd', 'fre', 'glk', 'lkm']
        with raises(TypeError):
            finder = Finder(string_list)
            assert finder.find(123) == ['asd']

    def test_bad_string2dict_type(self):
        string_list = [123, 'asdd', 'fre', 'glk', 'lkm']
        with raises(TypeError):
            finder = Finder(string_list)
            assert finder.find('asd') == ['asd']
