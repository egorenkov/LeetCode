class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return nums
        if len(nums) == 1:
            return [str(nums[0])]

        l = 0
        res = []
        for r in range(len(nums)-1):
            if nums[r] == nums[r+ 1] -1:
                continue
            else:
                if nums[l] == nums[r]:
                    res.append(str(nums[l]))
                    l = r + 1
                else:
                    res.append(str(nums[l]) + "->" + str(nums[r]))
                    l = r + 1
        if nums[l] == nums[r + 1]:
            res.append(str(nums[l]))
        else:
            res.append(str(nums[l]) + "->" + str(nums[r + 1]))
            
        return res
