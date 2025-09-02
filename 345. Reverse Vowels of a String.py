class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        glas = set('aeiouAEIOU')

        temp = []
        for el in s:
            if el in glas:
                temp.append(el)
        ans = []
        for i in range(len(s)):
            if s[i] in glas:
                a = temp.pop()
                ans.append(a)
            else:
                ans.append(s[i])
        return "".join(ans)
