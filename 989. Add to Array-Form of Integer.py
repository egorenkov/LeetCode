class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """

        ch = 0
        
        n = len(num) - 1
        for i in range(n + 1):
            ch += num[i] * 10 ** (n - i)
        
        ch += k
        ans = []
        while ch > 0:
            ans.append(ch % 10)
            ch /= 10
        return ans[::-1]
