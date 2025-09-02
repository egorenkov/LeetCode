class Solution(object):
    def rob(self, nums):
        def rob_linear(arr):
            prev, curr = 0, 0
            for num in arr:
                prev, curr = curr, max(curr, prev + num)
            return curr
        
        if not nums:
            return 0
        if len(nums) <= 3:
            return max(nums)
        
        # Максимум из двух случаев:
        # 1. Берем первый, не берем последний
        # 2. Не берем первый, берем последний
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
