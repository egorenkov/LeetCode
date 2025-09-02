# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        return solve(root)

def solve(root):
    if root is None: return None
    def run(node):
        if node is None:
            return 
        node.left, node.right = node.right, node.left
        run(node.left)
        run(node.right)

        return node    
    return run(root)
