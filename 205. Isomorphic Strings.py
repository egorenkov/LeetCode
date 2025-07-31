class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        temp1 ={}
        temp2 = {}
        for i in range(len(s)):
            if s[i] not in temp1:
                temp1[s[i]] = t[i]
            if t[i] not in temp2:
                temp2[t[i]] = s[i]
            if temp1[s[i]] != t[i] or temp2[t[i]] != s[i]:
                return False
        return True
        
