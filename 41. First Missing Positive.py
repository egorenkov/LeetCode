class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)

        for i in range(N):
            if nums[i] <= 0 or nums[i] > N:
                nums[i] = N + 1
            
        
        for i in range(N):
            num = abs(nums[i])
            if 0 < num <= N:
                nums[num - 1] = -abs(nums[num - 1])   

        for i in range(N):
            if nums[i]>0:
                return i + 1

        return N + 1     





