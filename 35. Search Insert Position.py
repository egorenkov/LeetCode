class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target <= nums[0]:
            return 0
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r + 1) // 2
            if target <= nums[mid]:
                r = mid -1
            else:
                l = mid 
        return l +1
