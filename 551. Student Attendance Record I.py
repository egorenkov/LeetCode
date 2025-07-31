class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = 0
        l = 0
        l_m = 0
        for el in s:
            if el =="A":
                a += 1
                l = 0
            elif el == "L":
                l+= 1
            else:
                l = 0
            
            if l == 3 or a >= 2:
                return False
        return True
    
