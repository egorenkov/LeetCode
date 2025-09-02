class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        curr_el = 0
        for i in range(len(nums)):
            if curr_el == 0:
                res = nums[i]
            
            curr_el += 1 if nums[i] == res else -1
        return res
        """
        Идея:
        Если число встречается часто, то 
        оно точно будет в результате
        """






        """
        N = len(nums)
        temp = {}

        for i in nums:
            if i not in temp:
                temp[i] = 0
            temp[i] += 1
        
        for k, v in temp.items():
            if v > N /2:
                return k
        return 
        """
