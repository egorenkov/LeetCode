class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0 , len(numbers) - 1
        while l <= r:
            m = numbers[l] + numbers[r]
            if m > target:
                r -= 1
            elif m < target:
                l += 1
            else:
                return [l + 1, r + 1]

        
