from finder import Finder


print("Solution Demonstration")
string_list = ['asd', 'asdd', 'fre', 'glk', 'lkm']
print("string_list: ", string_list)
finder = Finder(string_list)
found = finder.find('sad')
print("finder.find('sad'): ", found)
