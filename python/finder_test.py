import unittest
from finder import Finder


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