class Solution(object):
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expand(l,r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l +1:r]
        maxi = ""
        for i in range(len(s)):
            neChet = expand(i,i)
            chet = expand(i, i+1)
            maxi = max(maxi, neChet, chet, key = len)
        return maxi
