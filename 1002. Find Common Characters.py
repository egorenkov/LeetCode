class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # Инициализируем массив частот первого слова
        arr = [0] * 26
        for ch in words[0]:
            arr[ord(ch) - ord('a')] += 1
        
        # Для каждого следующего слова обновляем arr, оставляя минимумы
        for word in words[1:]:
            temp = [0] * 26
            for ch in word:
                temp[ord(ch) - ord('a')] += 1
            
            # Берем минимум между arr и temp
            for i in range(26):
                arr[i] = min(arr[i], temp[i])
        
        # Формируем результат
        ans = []
        for i in range(26):
            for _ in range(arr[i]):
                ans.append(chr(i + ord('a')))
        
        return ans
        

                    
