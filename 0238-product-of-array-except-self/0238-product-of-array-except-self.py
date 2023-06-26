class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1, 2, 6, 24
        #24, 24, 12, 4

        pre = []
        post = []
        res = []
        n = 1
        for num in nums:
            n *= num
            pre.append(n)
        
        n = 1
        for num in nums[::-1]:
            n *= num
            post.append(n)
        post.reverse()

        for index, num in enumerate(nums):
            n = pre[index - 1] if index > 0 else 1
            n2 = post[index + 1] if index < len(nums) - 1 else 1
            res.append(n * n2)
        
        return res
