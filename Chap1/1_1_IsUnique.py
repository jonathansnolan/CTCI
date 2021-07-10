import unittest

def IsUnique(s):
    x = list(dict.fromkeys(s))
    for k in x:
        if s.count(k) > 1:
            return False

    return True
