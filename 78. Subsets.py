class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return solve(nums)


def solve(nums):

    def run(seq, k):
        if k == 0:
            return [[]]
        
        res = []
        for i in range(len(seq)):
            for el in run(seq[i+1 :], k - 1):
                res.append([seq[i]] + el)
        return res

    N = len(nums)
    ans = [[]]
    for i in range(1,N + 1):
        ans.extend(run(nums, i))

    return ans
