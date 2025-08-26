class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return solve(n,k)

def solve(n,k):
    
    def run(a,b,c):
        if c == 0:
            return [[]]

        result = []

        for i in range(a,b):
            for el in run(i + 1, b, c - 1):
                result.append([i] + el)

        return result

    return run(1, n + 1, k)
