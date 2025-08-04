class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        temp = {}
        for i in range(len(nums)):
            if nums[i] not in temp:
                temp[nums[i]] = 0
            temp[nums[i]] += 1
    
        sor = sorted(temp.items(), key = lambda x : x[1], reverse = True)
        res = []
        for i in range(k):
            res.append(sor[i][0])
        return res
        
        
