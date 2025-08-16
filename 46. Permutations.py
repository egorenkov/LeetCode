class Solution(object):
    def generate_tuples(self, seq, n):
        if n == 0:
            return [[]]  # список с одним пустым кортежём

        result = []
        for i in range(len(seq)):
            for sub_tuple in self.generate_tuples(seq[:i] + seq[i+1:], n - 1):
                result.append([seq[i]] + sub_tuple)
        return result

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.generate_tuples(nums, len(nums))
