# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self, node, check_arr): 
        if node is None:
            return
        check_arr.append(node.val)

        self.dfs(node.left, check_arr)
        self.dfs(node.right, check_arr)

        return
    
    
    def findMode(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        arr = []
        self.dfs(root,arr)
        temp = dict()
        for i in arr:
            if i not in temp:
                temp[i] = 0
            temp[i] += 1

        m = -1
        res = []
        for v in temp.values():
            if v > m:
                m = v

        for k, v in temp.items():
            if v == m:
                res.append(k)

        return res
    
