class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = s.upper()
        s = "".join(s.split("-"))
        l = len(s)
        res = ""
        if l % k != 0:

            res += s[0:l%k] + '-'
        for i in range(l %k, l - k+1,k):
            res += s[i:i+k] + "-"
        return res[:-1]
        
