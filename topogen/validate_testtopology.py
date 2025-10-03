def validate(graph: list[list[int]], n: int) -> bool:
    """Validate that the graph is a line (path) topology of n nodes.

    Args:
        graph (list[list[int]]): Adjacency list representation of the graph.
        n (int): Expected number of nodes.

    Returns:
        bool: True if the graph is a valid line topology, False otherwise.
    """
    if len(graph) != n:
        return False

    # Check degrees
    degrees = [len(neighbors) for neighbors in graph]

    if n == 1:
        if degrees[0] != 0:
            return False
    elif n == 2:
        if degrees != [1, 1]:
            return False
    else:
        if degrees.count(1) != 2:  # exactly two endpoints
            return False
        if degrees.count(2) != n - 2:  # all others degree 2
            return False

    # Check connectivity with DFS/BFS
    visited = set()
    stack = [0]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node])

    return len(visited) == n