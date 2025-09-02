class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mySet = set()
        for i in range(len(nums)):
            if nums[i] in mySet:
                return True
            mySet.add(nums[i])
    
        return False
