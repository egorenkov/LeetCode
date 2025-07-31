class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        b_maxi = bin(max(x,y))[2:][::-1]
        b_mini = bin(min(x,y))[2:][::-1]
        res = 0
        for i in range(len(b_mini)):
            if b_maxi[i] != b_mini[i]:
                res += 1

        
        res += b_maxi[len(b_mini):].count('1')
        return res
