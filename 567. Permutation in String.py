class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        target = "".join(sorted(s1))

        for i in range(0,len(s2) - len(s1) +1):
            if target == "".join(sorted(s2[i:i+ len(s1)])):
                return True
        return False
        
