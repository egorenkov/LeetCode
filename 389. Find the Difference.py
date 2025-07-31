class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        s1 = 0
        s2 = 0
        for i in s:
            s1 += ord(i)
        for i in t:
            s2 += ord(i)

        return chr(s2 - s1)
