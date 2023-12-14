import unittest
import tsp

class TestOperations(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(tsp.addition(3, 2) == 5, True, "Should be True")
    def test_2(self):
        self.assertEqual(tsp.addition(7, 7) == 15, False, "Should be False")
    def test_3(self):
        self.assertNotEqual(tsp.addition(14, 2) == 2, True, "Should be not True")
        
if __name__=='__main__':
    unittest.main()