class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def run(x,n):

            if n < 0:
                n = -n
                x = 1/x
            if n == 1:
                return x
            result = 1.0
            while n :

                if n & 1: result *= x
                x = x **2
                n = n >>1
            return result
        return run(x,n)
