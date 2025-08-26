# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        return solve(p,q)


def solve(r1,r2):

    if (r1 is None) ^ (r2 is None):
        return False
    if not(r1) and not(r2):return True

    if r1.val == r2.val:
        return solve(r1.left, r2.left) and solve(r1.right, r2.right)
    
    return False
