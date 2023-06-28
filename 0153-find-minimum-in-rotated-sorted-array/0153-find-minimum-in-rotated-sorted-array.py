class Solution:
    def findMin(self, nums: List[int]) -> int:
        #bin search but if m > r then we know the pivot is somewhere between then
        # if m < l then we know the pivot is somewhere between that. 
        #we cut the array in half and can search for the minimum. 
        res = nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res


