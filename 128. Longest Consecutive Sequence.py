class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return solve(nums)
        
def brute(nums):
    if not nums: return 0

    nums.sort()
    ans = 1
    maxi = 1
    for i in range(len(nums)- 1):
        if nums[i+1] - nums[i] == 1:
            ans += 1
            maxi = max(ans,maxi)
        elif nums[i+1] - nums[i] == 0:
            pass
        else:
            ans = 1
    return maxi

def solve(seq):

    st = set(seq)
    ans = 0

    for el in st:

        if (el- 1) not in st:
            ln = 0
            while el + ln in st:
                ln += 1
             
            ans = max(ln,ans)
    return ans
