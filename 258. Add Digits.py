class Solution(object):

    def rec(self, num):

        arr = []
        while num > 0:
            arr.append(num % 10)
            num = num // 10
        if len(arr) == 0:
            return 0
        if len(arr) == 1:
            return sum(arr)
        return self.rec(sum(arr))



    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return self.rec(num)
        
