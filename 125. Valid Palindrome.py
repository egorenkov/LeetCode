class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        res = ""
        s = s.lower()
        for i in s:
            if i.isalpha() or i.isnumeric():
                res  = res + i

        return res == res[::-1]
