'''
You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.
Return the number of servers that communicate with any other server.
Example 1:
Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.
Example 2:
Input: grid = [[1,0],[1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.
Example 3:
Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4
Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.
'''




class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        rc = [0]*r
        cc = [0]*c
        for i in range(r):
            for j in range(c):
                if grid[i][j]:
                    rc[i] += 1
                    cc[j] += 1
        ans = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] and (rc[i] > 1 or cc[j] > 1):
                    ans += 1
        return ans
