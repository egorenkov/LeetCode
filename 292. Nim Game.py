class Solution:
    def canWinNim(self, n):
        # Выигрышная позиция только когда камни не кратны 4
        return n % 4 != 0
