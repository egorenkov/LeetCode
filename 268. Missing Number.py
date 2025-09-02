class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = sum([i for i in range(0, n + 1)])
        return res - sum(nums)
