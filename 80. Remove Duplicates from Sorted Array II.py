class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 1
        prev = nums[0]
        
        ans = 0

        for i in range(1, len(nums)):
            if nums[i] == prev:
                k += 1
                if k >= 3:
                    nums[i] = None
                    ans += 1
            else:
                prev = nums[i]
                k = 1
        
        ind = 0
        for i in range(len(nums)):
            if nums[i] is not None:
                nums[ind] = nums[i]
                ind += 1  
        return len(nums) - ans

        
