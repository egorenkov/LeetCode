class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """

        if num == 0:
            return str(num)
        nums = abs(num) 
        r = ""
        while nums > 0:
            r += str(nums %  7)
            nums //= 7
        return r[::-1] if num > 0 else "-" +r[::-1]
