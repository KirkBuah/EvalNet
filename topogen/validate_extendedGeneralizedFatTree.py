# Copyright (c) 2025 ETH Zurich.
#                    All rights reserved.
#
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# Main author: Jascha Krattenmacher

# validate a created extended Generalized Fat Tree

from .common import has_double_edges, is_directed, listgraph_to_nxgraph
from networkx import Graph, is_connected
from networkx.classes.function import degree
from random import randint


def validate(graph : [[int]], h : int, inputs : [int]):
    print("--> Validating %dh-extendedGeneralizedFatTree[%s][%s]:" %(h,".".join(str(i) for i in inputs[:h]), ".".join(str(i) for i in inputs[h:]) ) )
    passed = 1

    # check for double edges
    if has_double_edges(graph):
        print("     --> construction error: has double edges")
        passed = 0

    # construct a NetworkX graph (undirected, no multi-edges) for further validation
    nx_graph = listgraph_to_nxgraph(graph)

    # check if graph is connected
    if not is_connected(nx_graph):
        print("     --> construnction error: not conncected")
        passed = 0

    return passed

def generate_random_parameters(hmax : int, m2max : int, w2max : int, number : int):
    parameters = []
    for _ in range(number):
        h = randint(1, hmax)
        m2 = randint(1,m2max)
        m1 = randint(1, m2)
        w2 = randint(1, w2max)
        w1 = randint(1, w2)
        parameters.append((h,m1,m2,w1,w2))
    
    return parameters

def validate_extendedGeneralizedFatTree():
    from .ExtendedGeneralizedFatTreeGenerator import ExtendedGeneralizedFatTreeGenerator

    extendedGeneralizedFatTrees = generate_random_parameters(5,5,3,5)

    results = []
    for ft in extendedGeneralizedFatTrees:
        g = ExtendedGeneralizedFatTreeGenerator().make(ft)
        results.append(validate(g, ft))
    
    if sum(results) == len(extendedGeneralizedFatTrees):
        print("VALIDATION PASSED")
    else:
        print("VALIDATION NOT PASSED")
