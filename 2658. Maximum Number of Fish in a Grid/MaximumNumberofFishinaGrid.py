'''
You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:

A land cell if grid[r][c] = 0, or
A water cell containing grid[r][c] fish, if grid[r][c] > 0.
A fisher can start at any water cell (r, c) and can do the following operations any number of times:

Catch all the fish at cell (r, c), or
Move to any adjacent water cell.
Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.

An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.

 

Example 1:


Input: grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
Output: 7
Explanation: The fisher can start at cell (1,3) and collect 3 fish, then move to cell (2,3) and collect 4 fish.
Example 2:


Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
Output: 1
Explanation: The fisher can start at cells (0,0) or (3,3) and collect a single fish. 



'''





class Solution:
    # Helper function to count the number of fishes in a connected component
    def calculate_fishes(self, grid, visited, row, col):
        # Check boundary conditions, water cells, or already visited cells
        if (
            row < 0
            or row >= len(grid)
            or col < 0
            or col >= len(grid[0])
            or grid[row][col] == 0
            or visited[row][col]
        ):
            return 0

        # Mark the current cell as visited
        visited[row][col] = True

        # Accumulate the fish count from the current cell and its neighbors
        return (
            grid[row][col]
            + self.calculate_fishes(grid, visited, row, col + 1)
            + self.calculate_fishes(grid, visited, row, col - 1)
            + self.calculate_fishes(grid, visited, row + 1, col)
            + self.calculate_fishes(grid, visited, row - 1, col)
        )

    def findMaxFish(self, grid):
        rows, cols = len(grid), len(grid[0])
        max_fish_count = 0

        # A 2D list to track visited cells
        visited = [[False] * cols for _ in range(rows)]

        # Iterate through all cells in the grid
        for row in range(rows):
            for col in range(cols):
                # Start a DFS for unvisited land cells (fish available)
                if grid[row][col] > 0 and not visited[row][col]:
                    max_fish_count = max(
                        max_fish_count,
                        self.calculate_fishes(grid, visited, row, col),
                    )

        # Return the maximum fish count found
        return max_fish_count
