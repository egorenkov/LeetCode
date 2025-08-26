class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        basket = [0 for i in range(3)]
        for i in range(len(nums)):
            basket[nums[i]] += 1
        
        it = 0
        for i in range(len(basket)):
            for j in range(basket[i]):
                nums[it] = i
                it += 1
