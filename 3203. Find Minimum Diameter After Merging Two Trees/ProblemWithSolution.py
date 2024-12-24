'''
There exist two undirected trees with n and m nodes, numbered from 0 to n - 1 and from 0 to m - 1, respectively. You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, 
where edges1[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the second tree.
You must connect one node from the first tree with another node from the second tree with an edge.
Return the minimum possible diameter of the resulting tree.
The diameter of a tree is the length of the longest path between any two nodes in the tree.
Example 1:
Input: edges1 = [[0,1],[0,2],[0,3]], edges2 = [[0,1]]
Output: 3
Explanation:
We can obtain a tree of diameter 3 by connecting node 0 from the first tree with any node from the second tree.\
Example 2:
Input: edges1 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]], edges2 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]
Output: 5
Explanation:
We can obtain a tree of diameter 5 by connecting node 0 from the first tree with node 0 from the second tree.
Constraints:

1 <= n, m <= 105
edges1.length == n - 1
edges2.length == m - 1
edges1[i].length == edges2[i].length == 2
edges1[i] = [ai, bi]
0 <= ai, bi < n
edges2[i] = [ui, vi]
0 <= ui, vi < m
The input is generated such that edges1 and edges2 represent valid trees.
'''

class Solution:
    def minimumDiameterAfterMerge(
        self, edges1: list[list[int]], edges2: list[list[int]]
    ) -> int:
        # Calculate the number of nodes for each tree (number of edges + 1)
        n = len(edges1) + 1
        m = len(edges2) + 1

        # Build adjacency lists for both trees
        adj_list1 = self.build_adj_list(n, edges1)
        adj_list2 = self.build_adj_list(m, edges2)

        # Calculate the diameter of both trees
        diameter1, _ = self.find_diameter(
            adj_list1, 0, -1
        )  # Start DFS for Tree 1
        diameter2, _ = self.find_diameter(
            adj_list2, 0, -1
        )  # Start DFS for Tree 2

        # Calculate the diameter of the combined tree
        # This accounts for the longest path spanning both trees
        combined_diameter = ceil(diameter1 / 2) + ceil(diameter2 / 2) + 1

        # Return the maximum diameter among the two trees and the combined tree
        return max(diameter1, diameter2, combined_diameter)

    # Helper function to build an adjacency list from an edge list
    def build_adj_list(
        self, size: int, edges: list[list[int]]
    ) -> list[list[int]]:
        adj_list = [[] for _ in range(size)]
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        return adj_list

    # Helper function to find the diameter of a tree
    # Returns the diameter and the depth of the node's subtree
    def find_diameter(
        self, adj_list: list[list[int]], node: int, parent: int
    ) -> tuple[int, int]:
        max_depth1 = max_depth2 = (
            0  # Tracks the two largest depths from the current node
        )
        diameter = 0  # Tracks the maximum diameter of the subtree

        for neighbor in adj_list[node]:
            if neighbor == parent:
                continue  # Skip the parent to avoid cycles

            # Recursively calculate the diameter and depth of the neighbor's subtree
            child_diameter, depth = self.find_diameter(adj_list, neighbor, node)
            depth += 1  # Increment depth to include edge to neighbor

            # Update the maximum diameter of the subtree
            diameter = max(diameter, child_diameter)

            # Update the two largest depths from the current node
            if depth > max_depth1:
                max_depth2 = max_depth1
                max_depth1 = depth
            elif depth > max_depth2:
                max_depth2 = depth

        # Update the diameter to include the path through the current node
        diameter = max(diameter, max_depth1 + max_depth2)

        # Return the diameter and the longest depth
        return diameter, max_depth1
