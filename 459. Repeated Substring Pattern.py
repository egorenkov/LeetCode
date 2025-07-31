class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
       

        for i in range(1,len(s) // 2 + 1):
            f = True
            if len(s) % i != 0:
                continue
            arr =[j for j in range(0,len(s), i)]
            if len(arr) <= 1:
                continue
            if len(arr) < 3:
                if s[arr[0]: arr[1]] != s[arr[1] :]:
                    f = False
            arr.append(len(s))   
            for j in range(len(arr) - 2):
                if s[arr[j] : arr[j+ 1]] != s[arr[j+1] : arr[j+ 2]]:
                    f = False
                    break
            if f:
                return True
        return False
