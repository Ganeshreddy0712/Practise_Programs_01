import unittest

question_01 = ''' Python script that takes two integer values and returns True if n is a multiple of m, 
that is, n = mi for some integer i, and False otherwise.'''


def is_multiple(n, m):
    if n==0 or m==0:
        return False
    else:
     if n%m==0:
        return True
     else:
        return False        
    pass
        


class TestIsMultiple(unittest.TestCase):

    def test_01(self):
        self.assertEqual(is_multiple(4,2), True)

    def test_02(self):
        self.assertEqual(is_multiple(4,3),False) 
     
    def test_03(self):
        self.assertEqual(is_multiple(2,4),False) 
       
    def test_04(self):
        self.assertEqual(is_multiple(4,0),False) 

    def test_05(self):
        self.assertEqual(is_multiple(0,3),False) 


if _name_ == '_main_':
    unittest.main(verbosity=2)
