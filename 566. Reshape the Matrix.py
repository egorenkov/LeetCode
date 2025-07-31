class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """

        

        prev_r = len(mat)
        prev_c = len(mat[0])
        if prev_r * prev_c != c *r :
            return mat

        temp = []
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                temp.append(mat[i][j])
            
        res = []
        cnt = 0
        for i in range(r):
            t = []
            for j in range(c):
                t.append(temp[cnt])
                cnt += 1
            
            res.append(t)

        return res
        
