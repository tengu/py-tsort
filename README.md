py-tsort
========

topological sort in python.
Topologically sort vertices in a DAG. 
Useful for dependency resolution.

>>> from tsort import topological_sort
>>> topological_sort([(7, 11), (7, 8), (5, 11), (3, 8), (3, 10), (8, 10), (11, 2), (11, 9), (11, 10), (8, 9)])
[3, 5, 7, 8, 11, 2, 9, 10]

