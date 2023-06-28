class Solution:
    def findMin(self, nums: List[int]) -> int:
        #bin search but if m > r then we know the pivot is somewhere between then
        # if m < l then we know the pivot is somewhere between that. 
        #we cut the array in half and can search for the minimum. 
        return min(nums)


