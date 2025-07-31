class Solution(object):
    def singleNonDuplicate(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in arr:
            res ^= i
        return res
        
        
