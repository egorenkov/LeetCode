# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root: return False
        if root.left is None and root.right is None:
            return True
        return solve(root.left, root.right)
        
def solve(r1,r2):
    if (r1 is None) ^ (r2 is None): return False
    if r1 is None and r2 is None:return True

    if r1 is not None and r2 is not None:
        if r1.val == r2.val:
            return solve(r1.left, r2.right) and solve(r1.right, r2.left)
        return False
    return False
