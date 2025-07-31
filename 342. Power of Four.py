class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        
        e = 4
        while e <= n:
            if e== n:
                return True
            e = e * 4
        
        return False
