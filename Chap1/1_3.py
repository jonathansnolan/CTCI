# -*- coding: utf-8 -*-
import unittest
def urlify_algo(str,n):
    x = str.rstrip()
    if len(x) != n:
        return "FUCK"
    return x.replace(" ", "%20")

    x = x.split(" ")
    i = ""
    for k in x:
        i += k + "%20"

    return i[:-3]


######################
print(urlify_algo("Mr John Smith   ",13))
print(urlify_algo("much ado about nothing", len("much ado about nothing")))


class Test(unittest.TestCase):
    """Test Cases"""

    test_cases = [
        ("much ado about nothing      ", "much%20ado%20about%20nothing"),
        ("Mr John Smith    ", "Mr%20John%20Smith"),
    ]
    testable_functions = [urlify_algo]

    def test_urlify(self):
        for urlify in self.testable_functions:
            for test_string, expected in self.test_cases:
                stripped_length = len(test_string.rstrip(" "))
                actual = urlify(test_string, stripped_length)
                assert actual == expected


if __name__ == "__main__":
    unittest.main()
