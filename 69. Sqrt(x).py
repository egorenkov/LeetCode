class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = 0
        r = x
        while l < r:
            mid = (l + r + 1) // 2
            if mid * mid > x:r = mid -1
            else: l = mid

        return l
       
