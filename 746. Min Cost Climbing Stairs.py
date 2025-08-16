class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) == 2:
            return min(cost)
        seq = cost
        for i in range(2, len(seq)):
            seq[i] = seq[i] + min(seq[i-1], seq[i-2])

        return min(seq[-2:])
