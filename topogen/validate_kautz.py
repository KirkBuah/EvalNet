# Copyright (c) 2025 ETH Zurich.
#                    All rights reserved.
#
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# Main author: Jascha Krattenmacher

# validate a created Kautz topology

from .common import has_double_edges, is_directed, listgraph_to_nxgraph
from networkx import is_connected
from networkx.classes.function import degree
from random import randint


def validate(graph : [[int]], b : int, n: int):
    print("--> Validating Kautz%d-%d:" %(b,n))
 
    # check sizes
    if len(graph) != (b+1)*b**(n-1):
        print("     --> construction error: incorrect number of nodes")
        return 0
    
    # check for double edges
    if has_double_edges(graph):
        print("     --> construction error: has double edges")
        return 0
    
    # construct a NetworkX graph (undirected, no multi-edges) for further validation
    nx_graph = listgraph_to_nxgraph(graph)

    # check if graph is connected
    if not is_connected(nx_graph):
        print("     --> construnction error: not conncected")
        return 0

    return 1

def generate_random_parameters(bmax : int, nmax : int,  number : int) -> [int]:
    parameters = []
    while len(parameters) != number:
        b = randint(2, bmax)
        n = randint(2, nmax)
        parameters.append((b,n))
    return parameters

def validate_kautz():
    from .KautzGenerator import KautzGenerator

    kautzs = generate_random_parameters(6,6,5)

    results = []
    for bn in kautzs:
        g = KautzGenerator().make(bn[0], bn[1])
        results.append(validate(g, bn[0], bn[1]))
    
    if sum(results) == len(kautzs):
        print("VALIDATION PASSED")
    else:
        print("VALIDATION NOT PASSED")
