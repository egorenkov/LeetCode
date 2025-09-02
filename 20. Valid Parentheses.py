class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []

        buck_open = ("{", "[", "(")
        buck_close = ("}", "]", ")")
        temp = {"}" : "{",
                ")" : "(",
                "]" : "[",
                }

        for i in range(len(s)):
            if s[i] in buck_open:
                stack.append(s[i])
            else:
                if not stack: return False
                el = stack.pop()
                if temp[s[i]] != el: return False

        return False if stack else True 
