class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, combo, t):
            if t == target:
                res.append(combo.copy())
                return
            if t > target or i >= len(candidates):
                return
            
            combo.append(candidates[i])
            dfs(i, combo, t + candidates[i])
            combo.pop()
            dfs(i + 1, combo, t)
            
            
        
        dfs(0, [], 0)
        return res