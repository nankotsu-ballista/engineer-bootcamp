class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x)
        for i in range(len(s) // 2):
            if s[i] != s[-(i + 1)]:
                return False
        return True
