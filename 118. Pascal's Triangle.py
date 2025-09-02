class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        return solve(numRows)

def solve(N):

    def factorial(n):
        if n == 1 or n == 0: return 1

        ans = 1
        for i in range(2,n+1):
            ans *= i
        return ans

    def sochetania(k,m):
        return factorial(m) / (factorial(k) * factorial(m-k))

    def generate(ch):
        arr = []
        for i in range(ch + 1):
            arr.append(sochetania(i,ch))
        return arr
    
    res = []
    for i in range(N):
        res.append(generate(i))
    return res
