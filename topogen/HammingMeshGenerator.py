from math import ceil

class Board:
    def __init__(self, rows: int, columns: int, start_index: int = 0):
        self.rows = rows
        self.cols = columns
        self.adjacency = {start_index + i: set() for i in range(rows * columns)}

        # dictionaries containing as key the row/column index, and as value the two
        # nodes at the edges of the row/column
        self.horizontal_edges = {i: [] for i in range(rows)}
        self.vertical_edges = {i: [] for i in range(columns)}

        self.make_board(start_index)

    def make_board(self, start_index: int = 0):
        for row in range(self.rows):
            for col in range(self.cols):
                node = start_index + row * self.cols + col

                if col == 0 or col == self.cols - 1:
                    self.horizontal_edges[row].append(node)

                if row == 0 or row == self.rows - 1:
                    self.vertical_edges[col].append(node)

                # Up neighbor
                if row > 0:
                    self.adjacency[node].add(start_index + (row - 1) * self.cols + col)

                # Down neighbor
                if row < self.rows - 1:
                    self.adjacency[node].add(start_index + (row + 1) * self.cols + col)

                # Left neighbor
                if col > 0:
                    self.adjacency[node].add(start_index + row * self.cols + (col - 1))

                # Right neighbor
                if col < self.cols - 1:
                    self.adjacency[node].add(start_index + row * self.cols + (col + 1))

class BoardMesh:
    def __init__(self, rows_per_board: int, cols_per_board: int, boards_horizontal: int, boards_vertical: int):
        self.rows_per_board = rows_per_board
        self.cols_per_board = cols_per_board
        self.boards_horizontal = boards_horizontal
        self.boards_vertical = boards_vertical

        self.total_edge_nodes = rows_per_board * cols_per_board * boards_horizontal * boards_vertical
        self.total_nodes = self.total_edge_nodes
        self.adjacency = {i: set() for i in range(self.total_edge_nodes)}

        # Map of boards, where the key is (row_the_board_is_in, col_the_board_is_in), and the value is a Board instance
        self.board_map = self._init_board_map()

        # If the number of row edge nodes is less than 64, connect them with a switch
        if self.boards_horizontal * 2 < 64:
            self.connect_board_rows_with_switch()
        else:
            # Define number of ports
            self.row_k = ceil(2 * (self.boards_horizontal ** (1/3)))
            # Add 1 if k is odd
            self.row_k += self.row_k % 2
            self.connect_board_rows_with_ft()

        # If the number of column edge nodes is less than 64, connect them with a switch
        if self.boards_vertical * 2 < 64:
            self.connect_board_cols_with_switch()
        else:
            # Define number of ports
            self.col_k = ceil(2 * (self.boards_vertical ** (1/3)))
            # Add 1 if k is odd
            self.col_k += self.col_k % 2
            self.connect_board_cols_with_ft()

    def _init_board_map(self) -> dict[any, Board]:
        # Create boards
        start_index = 0
        boards: list[Board] = []
        for _ in range(self.boards_horizontal * self.boards_vertical):
            boards.append(Board(self.rows_per_board, self.cols_per_board, start_index))
            start_index += self.cols_per_board * self.rows_per_board

        board_map = {}
        for board_row in range(self.boards_vertical):
            for board_col in range(self.boards_horizontal):
                board = boards.pop()
                # Add boards to board map
                board_map[(board_row, board_col)] = board

                # Update adjacency list
                self.adjacency = dict(list(self.adjacency.items()) + list(board.adjacency.items()))

        return board_map

    def connect_board_rows_with_switch(self):
        """Connect each row of the board using a switch. That is, add a node for each row within the boards,
        to which all edge nodes in the same row are connected. Then update the adjacency list"""

        switch_nodes = {}  # (board_row, row_idx) -> switch_index
        switch_index = self.total_nodes  # switches start after edge nodes

        for (row_the_board_is_in, col_the_board_is_in), board in self.board_map.items():
            for row_idx, edge_nodes in board.horizontal_edges.items():
                key = (row_the_board_is_in, row_idx)

                # Assign a switch index if this global row hasn't been assigned one yet
                if key not in switch_nodes:
                    switch_nodes[key] = switch_index
                    self.adjacency[switch_index] = set()
                    switch_index += 1

                # Connect all edge nodes of this row to the switch
                s_idx = switch_nodes[key]
                for node in edge_nodes:
                    self.adjacency[s_idx].add(node)
                    self.adjacency[node].add(s_idx)

        self.total_nodes += switch_index - self.total_nodes

    def connect_board_cols_with_switch(self):
        """Connect each column of the board using a switch. That is, add a node for each column within the boards,
        to which all edge nodes in the same column are connected. Then update the adjacency list"""

        switch_nodes = {}  # (board_row, row_idx) -> switch_index
        switch_index = self.total_nodes  # switches start after edge nodes

        for (row_the_board_is_in, col_the_board_is_in), board in self.board_map.items():
            for col_idx, edge_nodes in board.vertical_edges.items():
                key = (col_the_board_is_in, col_idx)

                # Assign a switch index if this global row hasn't been assigned one yet
                if key not in switch_nodes:
                    switch_nodes[key] = switch_index
                    self.adjacency[switch_index] = set()
                    switch_index += 1

                # Connect all edge nodes of this row to the switch
                s_idx = switch_nodes[key]
                for node in edge_nodes:
                    self.adjacency[s_idx].add(node)
                    self.adjacency[node].add(s_idx)

        self.total_nodes += switch_index - self.total_nodes

    def connect_board_rows_with_ft(self):
        """Builds a fat tree for each row, connecting only edge nodes"""
        # Create the required number of fat trees
        fat_trees = []
        for _ in range (self.boards_vertical * self.rows_per_board):
            fat_tree_data = self.make_fat_tree(self.row_k, self.total_nodes)
            # Update total number of nodes
            self.total_nodes = fat_tree_data[2]
            # Append fat tree data to fat tree list
            fat_trees.append(fat_tree_data)
            # Update self.adjacency
            self.adjacency = dict(list(self.adjacency.items()) + list(fat_tree_data[0].items()))

        # --- Make the connections between fat tree and row edge nodes ---

        rows_grouped: dict[tuple[int, int], list[int]] = {}
        for (row_the_board_is_in, col_the_board_is_in), board in self.board_map.items():
            for row_idx, edge_nodes in board.horizontal_edges.items():
                key = (row_the_board_is_in, row_idx)

                if key not in rows_grouped:
                    rows_grouped[key] = []

                # Fill a dict with (board_row, node_row) and list of edge nodes
                rows_grouped[key].extend(edge_nodes)

        # Connect the edge nodes to the leaf nodes of a fat tree. Each leaf of the fat tree must be connected to at most 2 nodes
        while fat_trees:
            _, ft_leaves, _ = fat_trees.pop()
            # Take one row group
            row_key, nodes = rows_grouped.popitem()

            # Iterate nodes in groups of k/2
            for i in range(0, len(nodes), self.row_k//2): # k is guaranteed to be even
                endpoints = nodes[i:i+self.row_k//2]
                if not ft_leaves:
                    break # no more fat-tree leaves available

                leaf = ft_leaves.pop(0) # take one leaf from fat tree

                # Connect each node in the pair to the leaf
                for node in endpoints:
                    self.adjacency[node].add(leaf)
                    self.adjacency[leaf].add(node)



    def connect_board_cols_with_ft(self):
        """Builds a fat tree for each column, connecting only edge nodes"""
        # Create the required number of fat trees
        fat_trees = []
        for _ in range (self.boards_horizontal * self.cols_per_board):
            fat_tree_data = self.make_fat_tree(self.col_k, self.total_nodes)
            # Update total number of nodes
            self.total_nodes = fat_tree_data[2]
            # Append fat tree data to fat tree list
            fat_trees.append(fat_tree_data)
            # Update self.adjacency
            self.adjacency = dict(list(self.adjacency.items()) + list(fat_tree_data[0].items()))

        # --- Make the connections between fat tree and row edge nodes ---

        cols_grouped: dict[tuple[int, int], list[int]] = {}
        for (row_the_board_is_in, col_the_board_is_in), board in self.board_map.items():
            for col_idx, edge_nodes in board.vertical_edges.items():
                key = (col_the_board_is_in, col_idx)

                if key not in cols_grouped:
                    cols_grouped[key] = []

                # Fill a dict with (board_row, node_row) and list of edge nodes
                cols_grouped[key].extend(edge_nodes)

        # Connect the edge nodes to the leaf nodes of a fat tree. Each leaf of the fat tree must be connected to at most 2 nodes
        while fat_trees:
            _, ft_leaves, _ = fat_trees.pop()
            # Take one row group
            row_key, nodes = cols_grouped.popitem()

            # Iterate nodes in groups of k/2
            for i in range(0, len(nodes), self.col_k//2): # k is guaranteed to be even
                endpoints = nodes[i:i+self.col_k//2]
                if not ft_leaves:
                    break # no more fat-tree leaves available

                leaf = ft_leaves.pop(0) # take one leaf from fat tree

                # Connect each node in the pair to the leaf
                for node in endpoints:
                    self.adjacency[node].add(leaf)
                    self.adjacency[leaf].add(node)


    def make_fat_tree(self, k: int, node_id_start: int) -> tuple[dict, list, int]:
        """Build a fat-tree adjacency, return adjacency and leaves, offset by node_id_start."""
        assert k % 2 == 0
        p = k // 2
        n = 5 * p**2

        graph = {node_id_start + i: set() for i in range(n)}
        node_iter = iter(graph.keys())

        def p_square_group():
            return [[next(node_iter) for _ in range(p)] for __ in range(p)]

        edge_left  = p_square_group()
        edge_right = p_square_group()
        aggr_left  = p_square_group()
        aggr_right = p_square_group()
        core       = p_square_group()

        for ee, aa in [(edge_left, aggr_left), (edge_right, aggr_right)]:
            # edge ↔ aggregation
            for e, a in zip(ee, aa):
                for i in range(p):
                    for j in range(p):
                        graph[a[i]].add(e[j])
                        graph[e[j]].add(a[i])
            # aggregation ↔ core
            for c in core:
                for a in aa:
                    for i in range(p):
                        graph[c[i]].add(a[i])
                        graph[a[i]].add(c[i])

        leaves = edge_left + edge_right
        all_leaves = [leaf for row in leaves for leaf in row]
        return (graph, all_leaves, node_id_start + n)  # adjacency, leaf groups, next free ID