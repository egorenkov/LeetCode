class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        temp = sorted(nums)
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and temp[i] == temp[i-1]:
                continue
            j, k = i + 1, len(nums) -1
           
            while j < k:
                m = temp[i] + temp[j] + temp[k]
                if m > 0:
                    k -= 1
                elif m <0:
                    j += 1
                else:
                    res.append([temp[i] , temp[j] ,temp[k]])
                    j+=1
                   
                    while temp[j] == temp[j-1] and j < k:
                        j += 1
        return res
