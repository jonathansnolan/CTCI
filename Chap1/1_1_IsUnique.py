import unittest

#####################################
# This is the function itself
#####################################

def IsUnique(s):
    x = list(dict.fromkeys(s))
    for k in x:
        if s.count(k) > 1:
            return False

    if len(x) != len(s):
        return False

    return True


#####################################
# Here are tests to see see if the function works
#####################################

class Test(unittest.TestCase):
    test_cases = [
        ("abcd", True),
        ("s4fad", True),
        ("", True),
        ("23ds2", False),
        ("hb 627jh=j ()", False),
        ("".join([chr(val) for val in range(128)]), True),  # unique 128 chars
        ("".join([chr(val // 2) for val in range(129)]), False),  # non-unique 129 chars
    ]
    test_functions = [
        IsUnique
    ]

if __name__ == "__main__":
    unittest.main()
