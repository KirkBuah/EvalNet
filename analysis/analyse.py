# Copyright (c) 2025 ETH Zurich.
#                    All rights reserved.
#
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# Main author: Alessandro Maissen

from .InterferenceAnalysis import InterferenceAnalysis
from .ShortestPathAnalysis import ShortestPathAnalysis
from .EdgeDisjointPathAnalysis import EdgeDisjointPathAnalyis
from .common import make_topos
from os import makedirs, path


def analyse(topos: [str], classes: [int], jellyfish: bool, maxlength: int, analyse_function, parallel=False, sparse=False, lowmemory=False):
    networks = make_topos(topos, classes, jellyfish)

    if analyse_function == 'shortestpaths':
        ShortestPathAnalysis().analyse(networks=networks, maxlength=maxlength, sparse=sparse, parallel=parallel)
    elif analyse_function == 'disjointpaths':
        EdgeDisjointPathAnalyis().analyse(networks=networks, maxlength=maxlength)
    elif analyse_function == 'interference':
        InterferenceAnalysis().analyse(networks=networks, maxlength=maxlength)
    else:
        raise Exception('invalid analysis')
