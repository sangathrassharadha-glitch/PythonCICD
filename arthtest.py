from arth import*
import unittest
class ArthTest(unittest.TestCase):
    def test_add(self):
       self.assertEqual(add(10,5),15)
    def test_sub(self):
       self.assertEqual(sub(10,5),15)
    def test_mul(self):
       self.assertEqual(mul(10,5),15)
if __name__=="__ main__":
   unittest.mian()   
