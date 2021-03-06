class Finder():
    # returns a tuple with the input string and its char frequency dict
    @staticmethod
    def _string2dict(string):
        if not isinstance(string, str):
            raise TypeError

        adict = {}
        for char in string:
            if char not in adict:
                adict[char] = 1
            else:
                adict[char] = adict[char] + 1

        return (string, adict)

    def __init__(self, haystack):
        if not isinstance(haystack, list):
            raise TypeError

        # lets build a dict which groups strings in haystack by their
        # size in lists of tuples containing both the string
        # and its char frequency dictionary
        self._haystack = {}
        for x in haystack:
            if len(x) not in self._haystack:
                self._haystack[len(x)] = []
            self._haystack[len(x)].append(Finder._string2dict(x))

    def find(self, needle):
        if not isinstance(needle, str):
            raise TypeError

        needle, needle_dict = Finder._string2dict(needle)
        needle_size = len(needle)
        found = []
        if needle_size in self._haystack:
            for string, adict in self._haystack[needle_size]:
                if needle_dict == adict:
                    found.append(string)
        return found
