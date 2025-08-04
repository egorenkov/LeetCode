class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = len(s) - 1

        while l <= r:
           
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                without_l = s[0:l] + s[l+1:len(s)]
                without_r = s[0:r] + s[r+1:len(s)]
                return without_l == without_l[::-1] or without_r == without_r[::-1]

        return True
