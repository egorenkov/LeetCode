class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        check = strs[0]
        min_len = min(len(s) for s in strs)  # Ограничиваем длину минимальной строкой
        cnt = 0

        while cnt < min_len:
            for i in range(1, len(strs)):
                if check[cnt] != strs[i][cnt]:
                    return check[:cnt]
            cnt += 1

        return check[:min_len]  # Возвращаем только общую часть
