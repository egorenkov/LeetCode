class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        bine = bin(num)[2:]
        cnt =0
        res = 0
        for i in bine[::-1]:
            if i == "0":
                res+= pow(2, cnt)
            cnt += 1
        return res 
