class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        r1 = 0
        for i in num1:
            r1 = r1*10 + (ord(i) - 48)
        r2 = 0
        for i in num2:
            r2 = r2 * 10 + (ord(i) -  48)
        return str(r1 + r2)
        

        
