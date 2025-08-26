class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #return brute_force(nums,target)
        return binary_search(nums,target)

def brute_force(nums, target):
    ans = [-1,-1]

    if not nums:
        return ans

    l = -1
    r = -1
    i = 0
    while i < len(nums):
        if nums[i] == target:
            if l == -1:
                l = i
                r = i
            else:
                r = i

        i += 1

    return [l,r]

            
def binary_search(nums,target):

    N = len(nums)
    default = [-1,-1]

    def run():
        l, r = 0, N -1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                l = r = mid
                
              
                while l - 1 >= 0 and nums[l - 1] == target:
                    l -= 1
            
                while  r + 1 < N and nums[r + 1] == target :
                    r += 1
                    
                return [l, r ]

            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return default
    return run()

        
