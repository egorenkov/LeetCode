class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_int = 0
        for i in a:
            if i == "1": a_int = a_int * 2 + 1
            else: a_int *=2
        b_int = 0
        for i in b:
            if i == "1": b_int = b_int * 2 + 1
            else: b_int *=2
        
        z = a_int + b_int

        arr = []
        while z > 0:
            if z % 2 ==0:
                arr.append('0')
            else:
                arr.append('1')
            z = z //2
        if not arr:
            return '0'
        return ''.join(arr[::-1])
