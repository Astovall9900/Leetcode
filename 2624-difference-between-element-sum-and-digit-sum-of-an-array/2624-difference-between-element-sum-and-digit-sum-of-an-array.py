class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        #get digit sum
        #get element sum
        #return absolute difference |digit - element|
        #digit sum will usually be less than element sum
        digit = 0
        element = 0
        for num in nums:
            element += num
            dig = [*str(num)]
            for ele in dig:
                digit += int(ele)

        return element - digit


