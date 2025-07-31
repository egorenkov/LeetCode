class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True

        l = r = 0
        while r < len(t):
            if s[l] == t[r]:
                l += 1
            
            if l == len(s):
                return True

            r += 1

        return False
