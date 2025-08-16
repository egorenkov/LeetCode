class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        resArr = []
        l ,r = 0, 0

        while l < len(nums1) and r < len(nums2):
            if nums1[l] <= nums2[r]:
                resArr.append(nums1[l])
                l += 1
            else:
                resArr.append(nums2[r])
                r += 1

        while l < len(nums1):
            resArr.append(nums1[l])
            l += 1

        while r < len(nums2):
            resArr.append(nums2[r])
            r+=1
        

        if len(resArr) % 2 == 0:
            return (float(resArr[len(resArr) // 2 - 1]) + float(resArr[len(resArr) // 2 ])) / float(2)
        
        return float(  resArr[len(resArr)//2]   )
        
