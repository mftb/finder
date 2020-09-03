class Finder():
    # runs in O(N*M)
    def __init__(self, haystack):
        if not isinstance(haystack, list):
            raise TypeError

        # lets build a list of tuples containing both the string
        # and its char frequency dictionary for each string in haystack
        self._haystack = [Finder._string2dict(x) for x in haystack]

    # returns a tuple with the input string and its char frequency dict
    # runs in O(N)
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

    # runs in O(N)
    def find(self, needle):
        if not isinstance(needle, str):
            raise TypeError

        needle, needle_dict = Finder._string2dict(needle)
        found = []
        for string, adict in self._haystack:
            if needle_dict == adict:
                found.append(string)
        return found
