import unittest
from finder import Finder


class FinderLargeTests(unittest.TestCase):
    # large tests

    def test_large_constructor_list(self):
        large_list = ['abc' for i in range(0, 1000000)]
        finder = Finder(large_list)
        assert finder.find('abc') == large_list

    def test_10000_large_haystack_single_needle(self):
        large_list = [str(i) for i in range(0, 10000)]
        finder = Finder(large_list)
        assert finder.find('123') == ['123', '132', '213', '231', '312', '321']

    def test_100000_large_haystack_single_needle(self):
        large_list = [str(i) for i in range(0, 100000)]
        finder = Finder(large_list)
        assert finder.find('123') == ['123', '132', '213', '231', '312', '321']

    def test_1000000_large_haystack_single_needle(self):
        large_list = [str(i) for i in range(0, 1000000)]
        finder = Finder(large_list)
        assert finder.find('123') == ['123', '132', '213', '231', '312', '321']

    def test_10_sanity_checks(self):
        string_list = ['asd', 'asdd', 'fre', 'glk', 'lkm']
        finder = Finder(string_list)
        for i in range(0, 10):
            assert finder.find('sad') == ['asd']

    def test_100_sanity_checks(self):
        string_list = ['asd', 'asdd', 'fre', 'glk', 'lkm']
        finder = Finder(string_list)
        for i in range(0, 100):
            assert finder.find('sad') == ['asd']

    def test_1000_sanity_checks(self):
        string_list = ['asd', 'asdd', 'fre', 'glk', 'lkm']
        finder = Finder(string_list)
        for i in range(0, 100):
            assert finder.find('sad') == ['asd']

    def test_large_haystack_single_needle_10_finds(self):
        large_list = [str(i) for i in range(0, 10000)]
        finder = Finder(large_list)
        for n in range(0, 10):
            assert finder.find('123') == [
                '123', '132', '213', '231', '312', '321'
            ]
            assert finder.find('1111') == ['1111']
            assert finder.find('2222') == ['2222']

    def test_large_haystack_single_needle_100_finds(self):
        large_list = [str(i) for i in range(0, 10000)]
        finder = Finder(large_list)
        for n in range(0, 100):
            assert finder.find('123') == [
                '123', '132', '213', '231', '312', '321'
            ]
            assert finder.find('1111') == ['1111']
            assert finder.find('2222') == ['2222']

    def test_large_haystack_single_needle_1000_finds(self):
        large_list = [str(i) for i in range(0, 10000)]
        finder = Finder(large_list)
        for n in range(0, 1000):
            assert finder.find('123') == [
                '123', '132', '213', '231', '312', '321'
            ]
            assert finder.find('1111') == ['1111']
            assert finder.find('2222') == ['2222']

    def test_large_haystack_single_needle_10000_finds(self):
        large_list = [str(i) for i in range(0, 10000)]
        finder = Finder(large_list)
        for n in range(0, 10000):
            assert finder.find('123') == [
                '123', '132', '213', '231', '312', '321'
            ]
            assert finder.find('1111') == ['1111']
            assert finder.find('2222') == ['2222']
