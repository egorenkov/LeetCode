class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m1,m2 = max(nums[0], nums[1]), min(nums[0], nums[1])
        in1 , in2 = 0 if nums[0] > nums[1] else 1, 1 if nums[0] > nums[1] else 0 
        for i in range(2, len(nums)):
            if nums[i] > m1:
                m2 = m1
                m1 = nums[i]
                in2 = in1
                in1 = i
                
            elif nums[i] > m2:
                m2 = nums[i]
                in2 = i
            else :
                pass
        return in1 if m1 >= (m2 * 2) else -1
