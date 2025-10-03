from .TopologyGenerator import TopologyGenerator
from .validate_testtopology import validate

class TestTopologyGenerator(TopologyGenerator):
    def __init__(self):
        super(TestTopologyGenerator, self).__init__()

    def make(self, n: int) -> list[list[int]]:
        """Generate a line (path graph) of n nodes.

        Args:
            n (int): Number of nodes.

        Returns:
            list[list[int]]: Adjacency list of the line topology.
        """
        if n <= 0:
            return []

        adjacency = [[] for _ in range(n)]

        for i in range(n):
            if i > 0:
                adjacency[i].append(i - 1)  # connect left
            if i < n - 1:
                adjacency[i].append(i + 1)  # connect right

        return adjacency

    def validate(self, topo: [[int]], n: int) -> bool:
        return validate(topo, n)

    def get_folder_path(self):
        return super(TestTopologyGenerator,self).get_folder_path() + "test_topo/"

    def get_file_name(self, n : int) -> str:
        return "TestTopo." + str(n) + ".adj.txt"