# -*- coding: utf-8 -*-
import sys
import unittest
from tsort import topological_sort, GraphError

class Test(unittest.TestCase):

    def test_tsort(self):

        g="""
          7,11
          7,8
          5,11
          3,8
          3,10
          8,10
          11,2
          11,9
          11,10
          8,9
          """
        edges=[ tuple(map(int,e.split(','))) for e in g.strip().split('\n') ]
        print edges
        assert topological_sort(edges)==[3, 5, 7, 8, 11, 2, 9, 10]

        self.assertRaises(GraphError, topological_sort, (edges+[(9,3)]))

if __name__ == '__main__':

    unittest.main()
