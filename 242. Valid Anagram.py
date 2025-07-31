class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        arr1 = [0] * 26
        arr2 = [0] * 26

        for ch1 in s:
            arr1[ord(ch1) - 97] += 1
        for ch2 in t:
            arr2[ord(ch2) - 97] += 1
        for i in range(len(arr1)):
            if arr1[i] != arr2[i]:
                return False

        return True
        
