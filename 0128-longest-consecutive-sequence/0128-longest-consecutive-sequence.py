class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLen = 0
        for num in nums:
            if (num - 1) in numSet:
                continue
            count = 1
            n = num
            while n + 1 in numSet:
                count += 1
                n += 1
            maxLen = max(count, maxLen)
        return maxLen
            
            
