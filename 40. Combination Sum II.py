class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        
        def backtrack(start, current_sum):
            if current_sum == target:
                return [[]]
            
            if current_sum > target or start >= len(candidates):
                return []
            
            result = []
            for i in range(start, len(candidates)):
                
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                
                combinations = backtrack(i + 1, current_sum + candidates[i])
                for comb in combinations:
                    result.append([candidates[i]] + comb)
            
            return result
        
        return backtrack(0, 0)
