class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = dict()
        
        for i in range(len(nums)):
            m = target - nums[i]
            if m in dic:
                return [dic[m], i]
            dic[nums[i]] = i

        
