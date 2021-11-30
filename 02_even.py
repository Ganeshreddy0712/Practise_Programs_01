import unittest

question_02 = ''' Python script that takes an integer value k and returns True if k is even, and False otherwise. 
However, your function cannot use the multiplication, modulo, or division operators.'''


def is_even(k):
    if k%2==0:
        return True
    else:
        return False
    pass
        

class TestIsEven(unittest.TestCase):

    def test_01(self):
        self.assertEqual(is_even(2), True)

    def test_02(self):
        self.assertEqual(is_even(4),True) 
     
    def test_03(self):
        self.assertEqual(is_even(3),False) 
       
    def test_04(self):
        self.assertEqual(is_even(1),False) 

    def test_05(self):
        self.assertEqual(is_even(0),True) 


if _name_ == '_main_':
    unittest.main(verbosity=2)
