class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        elif x == int(str(x)[::-1]): return True
        else: return False
