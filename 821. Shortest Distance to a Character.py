class Solution(object):
    def shortestToChar(self, seq, t):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        ind = []
        for i in range(len(seq)):
            if seq[i] == t:
                ind.append(i)

        res = []
        for i in range(len(seq) ):
            mini = float('inf')
            for j in ind:
                if abs(i - j) < mini:
                    mini = abs(i - j)
            res.append(mini)

        return res
