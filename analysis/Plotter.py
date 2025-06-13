# Copyright (c) 2025 ETH Zurich.
#                    All rights reserved.
#
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os
class Plotter:
    def __init__(self):
        pass
    
    def plotted_topologies_info(self, plot_outfile, networks, preinfo=""):
        pre, _ = os.path.splitext(plot_outfile)
        info_outfile = pre + ".info"

        f=open(info_outfile,"w+")
        f.write(preinfo)
        for n in networks:
            f.write(n.get_info() + "\n")
