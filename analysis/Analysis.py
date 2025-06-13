# Copyright (c) 2025 ETH Zurich.
#                    All rights reserved.
#
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

from os import makedirs, path

class Analysis:
    datafilefolder = "data/analysis/"

    def __init__(self):
        if not path.exists(self.datafilefolder):
            makedirs(self.datafilefolder)

    def analyse(self, **kwargs):
        raise NotImplementedError
