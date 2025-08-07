class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        """
        new_arr = []
        i = 0
        j = 0
        while j < len(arr):
            if arr[i] == 0:
                new_arr.append(0)
                j += 1
                if j == len(arr):
                    break
                else:
                    new_arr.append(0)
            else:
                new_arr.append(arr[i])
            
            j += 1
            i += 1
        arr[:] = new_arr
        """
        zeros = arr.count(0)
        n = len(arr)
        for i in range(n-1, -1, -1):
            if i + zeros < n:
                arr[i + zeros] = arr[i]
            if arr[i] == 0:
                zeros -= 1
                if i + zeros < n:
                    arr[i + zeros] = 0

        
