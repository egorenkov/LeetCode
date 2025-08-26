class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # return solv(nums)
        return solv2(nums)
    
def solv(nums):
    INF = 10**10
    N = len(nums)

    @cache
    def run(idx):
        if idx < 0 or idx >= N: return False
        if idx == N -1: return True
        for i in range(1, nums[idx] +1):
            if idx + i < N and run(idx + i): return True
              
        return False


    return run(0)
    
def solv2(nums):

    N = len(nums)
    
    arr = [False for i in range(N)]

    def run(arr):
        
        for i in range(N -1 , -1, -1):
            if i == N - 1: arr[i] = True

            for j in range(1, nums[i] + 1):
                if i + j < N and arr[i + j] == True:
                    arr[i] = True
                    break
        return arr[0]

    return run(arr)
        
