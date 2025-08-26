class Solution(object):
    def divide(self, x, y):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if y == 0:
            raise "Divide by zero"
        if x == -2**31 and y == -1:
            return 2**31 - 1  # Ограничение 32-битного int
        
        flag = (x > 0) ^ (y > 0)

        a = abs(x)
        y = abs(y)

        ans = 0
        for i in range(32, -1, -1):
            if (y << i) <= a:
                a -= (y << i)
                ans += 2 ** i

        return ans if not flag else -ans
