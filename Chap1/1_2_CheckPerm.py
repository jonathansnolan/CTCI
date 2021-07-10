import unittest
from itertools import permutations
#####################################
# This is the function itself
#####################################

def CheckPerm(str1, str2):
    x = list(permutations(str1))
    i = []
    for k in x:
        y = ""
        for u in k:
            y += u
        i.append(y)


    if str2 in i:
        return True
    else:
        return False

#####################################
# Here are tests to see see if the function works
#####################################

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
        CheckPerm
    ]

    def test_cp(self):
        # true check
        for check_permutation in self.testable_functions:
            for str1, str2, expected in self.test_cases:
                assert check_permutation(str1, str2) == expected

if __name__ == "__main__":
    unittest.main()
