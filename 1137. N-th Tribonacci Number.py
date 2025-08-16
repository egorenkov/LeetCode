class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1

        T0 = 0
        T1 = 1
        T2 = 1

        while n > 2:
    
            T2, T0, T1  =T1 + T2 + T0, T1,T2 
            n -=1
            print(T2, T0,T1)

        
        return T2

cl = Solution()
print(cl.tribonacci(4))
