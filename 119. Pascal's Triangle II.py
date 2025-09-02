class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        return solve(rowIndex)

def solve(N):


    def fact(f):
        if f == 1 or f == 0: return 1
        ans = 1
        for i in range(2,f + 1):
            ans *= i
        return ans

    def C(m,k):
        return fact(k) / (fact(m) * fact(k - m))

    res = []
    for i in range(N+1):
        res.append(C(i,N))
    return res
