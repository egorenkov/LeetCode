class Solution(object):
    def __reverse(self,s):
        return s[::-1]


    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = s.split()
        return " ".join([self.__reverse(el) for el in arr])
        
