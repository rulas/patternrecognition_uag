'''
Created on Jun 22, 2013

@author: lrvillan
'''
from minimum_distance import *
from pylab import *
import unittest


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_distance_norm_1(self):
        a = ones((2,7)) *5
        result = distance_norm_1(a)
        expected = 0
        self.assertEqual(result, expected)
        
        a = array(([3,3,3,3],[5,5,5,5]))
        result = distance_norm_1(a)
        expected = 8
        self.assertEqual(result, expected)
        
    def test_distance_norm_2(self):
        a = ones((2,7)) *5
        result = distance_norm_2(a)
        expected = 0
        self.assertEqual(result, expected)
        
        a = array(([3,3,3,3],[5,5,5,5]))
        result = distance_norm_2(a)
        expected = 4
        self.assertEqual(result, expected)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()