class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        res = []
        pacific = set()
        atlantic = set()

        def dfs(r, c, height, visited):
            if (r < 0 or c < 0 or r >= ROWS or 
                c >= COLS or (r, c) in visited) or height > heights[r][c]:
                return
            
            visited.add((r, c))
            dfs(r + 1, c, heights[r][c], visited)
            dfs(r - 1, c, heights[r][c], visited)
            dfs(r, c + 1, heights[r][c], visited)
            dfs(r, c - 1, heights[r][c], visited)


        #run dfs on right and bottom to atlantic set
        #run dfs on top and left to pacific set
        for c in range(COLS):
            dfs(0, c, heights[0][c], pacific)
            dfs(ROWS - 1, c, heights[ROWS - 1][c], atlantic)

        for r in range(ROWS):
            dfs(r, 0, heights[r][0], pacific)
            dfs(r, COLS - 1, heights[r][COLS - 1], atlantic)
            
        for coordinates in pacific:
            if coordinates in atlantic:
                res.append(coordinates)
        
        return res
            


