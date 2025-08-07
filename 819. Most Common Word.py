class Solution(object):

    def preprocess(self, seq):
        tes = set("!?',;.")
        return "".join([char if char not in tes else " " for char in seq ]).lower()

    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        
        proc_seq = self.preprocess(paragraph).split()

        t_dict = {}
        for i in proc_seq:
            if i not in t_dict:
                t_dict[i] = 0
            t_dict[i] += 1
        
        ban = set(banned)
        m = -1
        res = None
        for k,v in t_dict.items():
            if k not in ban and v > m:
                res = k
                m = v
        return res
        
