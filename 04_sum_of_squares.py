import unittest

question_04 = ''' Python script that takes a positive integer n and returns the sum of the squares of all the positive integers smaller than n.'''


def sum_squares(n):
  pass
        


class TestSumSquares(unittest.TestCase):
  def test_01(self):
    self.assertEqual(sum_squares(4), 14)

  def test_02(self):
    self.assertEqual(sum_squares(9), 204)
     
  def test_03(self):
    self.assertEqual(sum_squares(1), 0)
   
  def test_04(self):
    self.assertEqual(sum_squares(2), 1)
    
  def test_05(self):
    self.assertEqual(sum_squares(100), 328350)
  
if __name__ == '__main__':
    unittest.main(verbosity=2)
