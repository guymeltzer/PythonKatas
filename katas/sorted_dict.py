class SortedDict(dict):
    """
    Implement SortedDict class which is a regular Python dictionary,
    but the keys are maintained in a sorted order

    Usage example:
    x = SortedDict()

    x['banana'] = 'ccc'
    x['apple'] = 'aaa'
    x['orange'] = 'bbb'

    list(x.keys())
    >> ['apple', 'banana', 'orange']

    list(x.values())
    >> ['aaa', 'ccc', 'bbb']

    list(x.items())
    >> [('apple', 'aaa'), ('banana', 'ccc'), ('orange', 'bbb')]
    """

    def __init__(self):
        super().__init__()
        self._sorted_keys = []

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        if key not in self._sorted_keys:
            self._sorted_keys.append(key)
            self._sorted_keys.sort()

    def items(self):
        return ((key, self[key]) for key in self._sorted_keys)

    def values(self):
        return (self[key] for key in self._sorted_keys)

    def keys(self):
        return iter(self._sorted_keys)


if __name__ == '__main__':

    s_dict = SortedDict()
    s_dict['a'] = None
    s_dict['t'] = None
    s_dict['h'] = None
    s_dict['q'] = None
    s_dict['b'] = None
    print(list(s_dict.items()))
