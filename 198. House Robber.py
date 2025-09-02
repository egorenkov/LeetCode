class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0 for i in range(len(nums) + 1)]
        dp[0], dp[1] = 0, nums[0]

        for i in range(1,len(nums)):
            dp[i+1] = max(dp[i-1]+ nums[i], dp[i])
        return dp[-1]
