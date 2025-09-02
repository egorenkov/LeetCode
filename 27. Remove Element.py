class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        ans = ["_"]* len(nums)
        ind = 0
        for i in range(len(nums)):
            if nums[i] != val:
                k += 1
                ans[ind] = nums[i]
                ind += 1
        nums[:] = ans
        return k            

        
