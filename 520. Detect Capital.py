class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) <= 0:
            return False

        if len(word) == 1:
            if  (65 <= ord(word[0])<= 90) or (97<= ord(word[0]) <= 122):
                return True
            return False

        
        if 65 <= ord(word[0]) <= 90:
            if 65 <= ord(word[1]) <= 90:
                for i in range(2,len(word)):
                    if not(65 <= ord(word[i]) <= 90):
                        return False
                return True
            elif 97 <= ord(word[1]) <= 122 :
                for i in range(2,len(word)):
                    if not(97 <= ord(word[i]) <= 122):
                        return False
                return True
            return False
            

        elif 97 <= ord(word[0]) <= 122 :
            for i in range(1,len(word)):
                if not (97 <= ord(word[i]) <= 122):
                    return False
            return True

        return False
