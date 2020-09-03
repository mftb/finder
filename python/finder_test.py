import unittest
from finder import Finder
from pytest import raises


class FinderTests(unittest.TestCase):
    ############################
    # ### setup and teardown ###
    ############################

    # executed prior to each test

    def setUp(self):
        pass

    # executed after each test
    def tearDown(self):
        pass

    def test_sanity_check(self):
        string_list = ['asd', 'asdd', 'fre', 'glk', 'lkm']
        finder = Finder(string_list)
        assert finder.find('sad') == ['asd']

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