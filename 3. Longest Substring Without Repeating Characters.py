class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mySet = set()

        l = 0
        maxi = 0
        for r in range(len(s)):       
            if s[r] in mySet:
                while s[r] in mySet:
                    if s[l] in mySet:
                        mySet.remove(s[l])
                    l += 1
            
            mySet.add(s[r])
            maxi = max(maxi, len(mySet))
        return maxi
