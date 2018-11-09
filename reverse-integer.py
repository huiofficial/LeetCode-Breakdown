class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0: x = -int(str(-x)[::-1])
        else: x = int(str(x)[::-1])
        if abs(x) > 2**31 or x == 0: return 0
        else: return x
