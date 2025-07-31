class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        

        res = []
        for i in range(int(sqrt(area)) + 1, 0 , -1):
            if area % i == 0:
                l = i
                r = area // i
                return [max(l,r),min(r,l)] 
