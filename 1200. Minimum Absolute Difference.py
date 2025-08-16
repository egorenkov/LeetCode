class Solution(object):

    def BinarySearch(self, seq, tar):
        l = 0
        r = len(seq) -1
        while l <= r:
            mid = (l + r) /2
            if seq[mid] > tar:
                r = mid - 1
            elif seq[mid] < tar:
                l = mid + 1
            else:
                return True
        return False  

    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        temp = sorted(arr)
        mini = float('inf')
        for i in range(len(temp) - 1):
            if mini > abs(temp[i] - temp[i+1]):
                mini = abs(temp[i] - temp[i+1])
        """
        res = []
        for i in range(len(temp) - 1):
            if self.BinarySearch(temp[i + 1:], mini + temp[i] ):
                res.append([temp[i] , mini + temp[i]])
        """
        res = [[temp[i] , temp[i + 1]] for i in range(len(temp) - 1) if temp[i + 1] - temp[i] == mini]

        return res
                
