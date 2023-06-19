class Solution:
    def isPalindrome(self, x: int) -> bool:
        sX = str(x)[::-1]
        return sX == str(x)