from collections import defaultdict
class Solution(object):
    def frequencySort(self, s):
        freq = defaultdict(int)
        for char in s:
            freq[char] += 1  # O(1) per operation
    
    # Создаём корзины: частота -> список символов
        buckets = [[] for _ in range(len(s) + 1)]  # Максимальная частота = len(s)
        for char, count in freq.items():
            buckets[count].append(char)  # Кладём символ в корзину с его частотой
    
    # Собираем результат, начиная с самых частых символов
        result = []
        for count in range(len(buckets) - 1, -1, -1):
            for char in buckets[count]:
                result.append(char * count)
    
        return ''.join(result)
