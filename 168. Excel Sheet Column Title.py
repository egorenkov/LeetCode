class Solution(object):
    def convertToTitle(self, num):
        """
        :type columnNumber: int
        :rtype: str
        """
        temp = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        
        res = []
        while num > 0:
            num -= 1  # добавляем эту строку
            res.append(temp[num % 26])  # меняем 25 на 26
            num = num // 26  # меняем 25 на 26
        return "".join(res[::-1])
