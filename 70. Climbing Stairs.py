class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        seq =  [1,1] + [0 for i in range(n-1)] 
        for i in range(2, len(seq)):
            seq[i] = seq[i-1] + seq[i -2]

        return seq[n]
