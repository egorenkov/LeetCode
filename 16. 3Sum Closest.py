class Solution(object):
    def threeSumClosest(self, arr, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if len(arr) == 3:
            return sum(arr)

        arr.sort()

        ans = float('inf')
        for i in range(len(arr) - 2):
            l, r = i + 1, len(arr) -1
            while l < r:
                total = arr[l] + arr[i] + arr[r]
                if abs(total - target) < abs(target - ans):
                    ans = total

                if  total > target:
                    r -= 1
                elif total < target:
                    l += 1
                else:
                    return target

        return ans




        """
        Baseline:
        ans = sum(arr[:3])
        for i in range(len(arr) - 2):
            for j in range(i + 1, len(arr) -1):
                for k in range(j +1, len(arr)):
                    if abs(target - ans) > abs(target - arr[i] - arr[j] - arr[k]):
                        ans = arr[i] + arr[j] + arr[k]

        return ans
        """
