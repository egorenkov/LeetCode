class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        ans = []
        stack = -1
        for i in range(len(arr)-1,-1,-1 ):
            ans.append(stack)
            if arr[i] > stack:
                stack = arr[i]
        return ans[::-1]
