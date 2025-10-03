from .Topology import Topology
from .Jellyfish import Jellyfish
from .TestTopologyGenerator import TestTopologyGenerator

class TestTopology(Topology):
    """
    Fields:
        Public:
            n: total number of nodes in the line
            r: maximum degree of a node (always 2 for line topology, except endpoints)
            R: total number of routers (same as n, since all are routers)
            N: total number of endnodes (same as n, since all nodes are endpoints in this simplified model)
            name: name of topology (default := Line)

        Private:
            __topo: holds None or the topology in adjacency list

    Methods:
        get_topo(): return the topology in adjacency list
        get_jellyfish_eq(): return jellyfish topology that uses same infrastructure
    """

    def __init__(self, n: int):
        if n < 1:
            raise Exception("Line topology must have at least 1 node")
        self.p = 1
        self.r = 2 if n > 2 else 1 if n == 2 else 0   # max degree in line
        self.R = n   # routers == nodes
        self.N = n   # treat every node as an endpoint
        self.nr = min(self.r - self.p, n - 1)  # network radix = degree - endnode links
        self.name = 'Line'
        self.edge = n

        # private fields
        self.__topo = None

    def get_topo(self):
        """Return the adjacency list of the line topology."""
        if self.__topo is None:
            self.__topo = TestTopologyGenerator().make(self.N)
        return self.__topo

    def get_jellyfish_eq(self):
        """Return a jellyfish topology with the same number of nodes/edges."""
        # In a line topology:
        # - edges = n-1
        # - avg degree ~ 2*(n-1)/n
        p = 1   # number of endnodes per router

        if self.R * self.nr % 2 != 0:
            self.nr -= 1
            p += 1

        assert self.r == self.p + self.nr or self.N <= 2

        jf = Jellyfish(self.nr, self.R, p)
        jf.name += "-" + self.name
        return jf