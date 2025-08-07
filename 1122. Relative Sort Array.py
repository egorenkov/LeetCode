class Solution(object):
    def relativeSortArray(self, arr, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        temp = {}
        for i in range(len(arr)):
            if arr[i] not in temp:
                temp[arr[i]] = 0
            temp[arr[i]] += 1
        ans = []
        for i in range(len(arr2)):
            for j in range(temp[arr2[i]]):
                ans.append(arr2[i])
            temp[arr2[i]] = 0

        temp = sorted(temp.items(), key = lambda x : x[0])
        for el in temp:
            if el[1] != 0:
                for i in range(el[1]):
                    ans.append(el[0])
        return ans
