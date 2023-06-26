class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #Dfs search and keep track of prev islands and current path
        #if current index is a part of a previous island then we dont start dfs
        #return number of islands
        ROWS, COLS = len(grid), len(grid[0])
        count = 0
        path = set()

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in path or grid[r][c] == "0"):
                return
            
            path.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in path:
                    continue
                if grid[r][c] == "1":
                    dfs(r, c)
                    count += 1


        return count