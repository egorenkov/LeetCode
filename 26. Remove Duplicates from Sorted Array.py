class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = nums[0] 
        i = 1
        cnt = len(nums)
        for j in range(1,len(nums)):
            if m == nums[j]:
                cnt -= 1
                continue
            else:
                nums[i] = nums[j]
                i += 1
                m = nums[j]
        k = len(nums) -1 
        while k > i:
            nums[k] = "_"
            k -= 1
        return cnt
            

