class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = len(bin(n)) - 3
        bins = []

        while n > 0:
            bins.append(n % 2)
            n //=2
        for i in range(32 -l ):
            bins.append(0)
        ans = 0
       
        for i in range(len(bins)):
            ans += bins[i] * (2 ** (32 - i - 1))
        return int(ans)
