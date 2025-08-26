# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def solve(node):
            if node is None:
                return 0
            return max(1 + solve(node.left), 1 + solve(node.right))
        return solve(root) 
        
