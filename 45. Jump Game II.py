from functools import cache

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return  solve(nums)

def solve(nums):
    
    INF = 10**10
    N = len(nums)

    @cache
    def run(idx):
        if idx >= N or idx < 0: return INF
        if idx == N -1:
            return 0 
        ans = INF
        for i in range(1, nums[idx] + 1):
            if idx + i < N :
                ans = min(ans, 1 + run(idx + i))
        return ans


    return run(0)
