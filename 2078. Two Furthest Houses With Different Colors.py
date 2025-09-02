class Solution(object):
    def maxDistance(self, nums):
        """
        :type colors: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) -1
        while nums[0] == nums[r]:
            r -= 1
        while nums[l] == nums[len(nums) - 1]:
            l += 1

        return max(r, len(nums) - l - 1)
