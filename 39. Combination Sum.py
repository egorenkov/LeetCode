class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return solve(candidates, target)
        
    
def solve(nums, targ):

    def run(seq, s):
        if s == targ:
            return [[]]
        if s > targ or len(seq) == 0:
            return [None]

        result = []
        for i in range(len(seq)):
            for el in run(seq[i:], s + seq[i]):
                if el is not None:
                    result.append([seq[i]] + el)   
                else:
                    break

        return result

    return run(nums,0)
       
