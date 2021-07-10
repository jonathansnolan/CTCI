import unittest
from itertools import permutations
#####################################
# This is the function itself
#####################################

def checkperm(x,y):
    # x and y are 2 strings

    if len(x) != len(y):
        return False
    #####################
    # Split the strings in to list
    #####################

    x = list(x.lower())
    y = list(y.lower())

    for k in x:
        if k in y and x.count(k) == y.count(k):
            continue
        else:
            return False

    for k in y:
        if k in x and x.count(k) == y.count(k):
            continue
        else:
            return False


    return True

class Test(unittest.TestCase):
    # str1, str2, is_permutation
    test_cases = (
        ("dog", "god", True),
        ("abcd", "bacd", True),
        ("3563476", "7334566", True),
        ("wef34f", "wffe34", True),
        ("dogx", "godz", False),
        ("abcd", "d2cba", False),
        ("2354", "1234", False),
        ("dcw4f", "dcw5f", False),
        ("DOG", "dog", False),
        ("dog ", "dog", False),
        ("aaab", "bbba", False),
    )

    testable_functions = [
        checkperm
    ]

    def test_cp(self):
        # true check
        for check_permutation in self.testable_functions:
            for str1, str2, expected in self.test_cases:
                assert check_permutation(str1, str2) == expected

if __name__ == "__main__":
    unittest.main()
