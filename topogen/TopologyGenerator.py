# Copyright (c) 2025 ETH Zurich.
#                    All rights reserved.
#
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# Main author: Alessandro Maissen

from os import path, makedirs

class TopologyGenerator():
    """
    This class acts as an interface/super class for a Topology Generator.
        
    To add support for a new topology subclass this and implement make, validate, get_file_name, get_folder_path.
    """

    def __init__(self):
        pass
    
    def make(self, **kwargs) -> [[int]]:
        """ 
        Implements the core function that generated the topology and returns it as a adjacency list.
        """
        raise NotImplementedError

    def validate(self, topo : [[int]], **kwargs) -> bool:
        """ 
        Implements the validation function that validates a generated topology. Returns True if validation is passed
        """
        raise NotImplementedError
    
    def get_file_name(self, **kwargs) -> str:
        """
        Specifies the filename of the file containg the topology
        """
        raise NotImplementedError
    
    def get_folder_path(self):
        return "data/"

    def generate(self, validate=False, save=False, **kwargs) -> [[int]]:
        print('--> Generating Topology')
        topo = self.make(**kwargs)

        if validate:
            if not self.validate(topo, **kwargs):
                raise Exception("Validation not passed")
            
        if save:
            filename = self.get_file_name(**kwargs)
            folderpath = self.get_folder_path()
            self.save(topo, folderpath, filename)
        
        return topo
    
    def save(self, topo, folderpath, filename):
        if not path.exists(folderpath):
            makedirs(folderpath)
        
        file = folderpath + filename

        with open(file, "w") as f:
            print(len(topo), int(sum(len(n) for n in topo) / 2), file=f)
            for node in topo:
                print( " ".join(str(e) for e in node) + " ", file=f)
        
        print('--> Saving to %s' % file)
