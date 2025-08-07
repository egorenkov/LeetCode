class Solution(object):

    def decodeFunc(self,s , temp):
        return "".join([temp[ord(let) - 97 ] for let in s])


    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
        "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        decode = {}
        for i in range(26):
            decode[i] = morse[i]
        
        new_words = set()
        for word in words:
            new_words.add(self.decodeFunc(word,decode))
        return len(new_words)
        
