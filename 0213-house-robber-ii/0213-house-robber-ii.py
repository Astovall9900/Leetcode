class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        mx = nums[0]
        for n in nums[:-1]:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        mx = max(mx, rob2)
        rob1 = 0
        rob2 = 0
        for n in nums[1:]:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        mx = max(mx, rob2)
        return mx