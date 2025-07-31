claclass Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join([i for i in s.strip().split(" ")[::-1] if i.strip() != ""])
