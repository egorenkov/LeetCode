class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        temp = {
            '2':'abc', 
            '3': "def", 
            '4': "ghi",
            '5': 'jkl' ,
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        if digits == '':
            return []

        result = ['']
        for digit in digits:
            result = [r + el for r in result for el in temp[digit] ]

        return result

  
