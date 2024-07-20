#!/usr/bin/env python
# -*- coding: utf-8 -*-

class GraphError(Exception):
    pass

def topological_sort(edges):
    """topologically sort vertices in edges.
    edges: list of pairs of vertices. Edges must form a DAG.
           If the graph has a cycle, then GraphError is raised.
    returns: topologically sorted list of vertices.
    see http://en.wikipedia.org/wiki/Topological_sorting
    """
    # resulting list
    L=[]

    # maintain forward and backward edge maps in parallel.
    st,ts={},{}

    def prune(s,t):
        del st[s][t]
        del ts[t][s]

    def add(s,t):
        try:
            st.setdefault(s,{})[t]=1
        except Exception as e:
            raise RuntimeError(e, (s,t))
        ts.setdefault(t,{})[s]=1

    for s,t in edges:
        add(s,t)

    # frontier
    S=set(st.keys()).difference(ts.keys())

    while S:
        s=S.pop()
        L.append(s)
        for t in st.get(s,{}).keys():
            prune(s,t)
            if not ts[t]:       # new frontier
                S.add(t)

    if filter(None, st.values()): # we have a cycle. report the cycle.
        def traverse(vs, seen):
            for s in vs:
                if s in seen:
                    raise GraphError('contains cycle: ', seen)
                seen.append(s) # xx use ordered set..
                traverse(st[s].keys(), seen)
        traverse(st.keys(), list())
        assert False, 'should not reach..'

    return L
