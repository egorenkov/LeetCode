class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False
        
        if x < 10:
            return True

        arr = []

        while x > 0:
            arr.append(x % 10)
            x //= 10
        
        for i in range(0 ,len(arr) // 2 + 1):
            if arr[i] != arr[-(i + 1)]:
                return False

        return True
