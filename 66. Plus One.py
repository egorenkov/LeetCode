class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        total = 1
        for i in range(len(digits)):
            total += digits[::-1][i] * (10**i)

        res = []
        while total > 0:
            res.append(total%10)
            total /= 10
        return res[::-1]

        
