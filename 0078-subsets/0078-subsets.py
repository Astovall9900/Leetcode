class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #result array and subset array
        res = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return 
            
            #left tree
            subset.append(nums[i])
            dfs(i + 1)

            #right tree
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res