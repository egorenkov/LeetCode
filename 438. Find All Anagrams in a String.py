class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        temp1 = dict()
        for i in p:
            if i not in temp1:
                temp1[i] = 0
            temp1[i] += 1

        temp2 = dict()
        for i in range(len(p)):
            if s[i] not in temp2:
                temp2[s[i]] = 0
            temp2[s[i]] += 1

        res = []
        if temp1 == temp2:
            res.append(0)

        for i in range(len(p), len(s) ):
            
            temp2[s[i - len(p)]] -= 1
            if temp2[s[i - len(p)]] == 0:
                temp2.pop(s[i - len(p)])
            if s[i] not in temp2:
                temp2[s[i]] = 0
            temp2[s[i]] += 1

            if temp2 == temp1:
                res.append(i - len(p) + 1)

        return res
