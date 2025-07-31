class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nt = set(nums)
        res = []
        for i in range(1,len(nums)+1):
            if i not in nt:
                res.append(i)
        return res

        
