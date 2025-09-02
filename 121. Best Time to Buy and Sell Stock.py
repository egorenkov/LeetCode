class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return solve(prices)

def brute_force(seq):
    ans = 0
    for i in range(len(seq)-1):
        for j in range(i + 1, len(seq)):
            if seq[j] -seq[i] > ans:
                ans = seq[j] - seq[i]
    return ans 


def solve(seq):
    def run(arr):
        best_price = arr[0]
        profit = 0

        for i in arr[1:]:
            if i < best_price:
                best_price = i

            profit = max(profit, i - best_price )
        return profit

