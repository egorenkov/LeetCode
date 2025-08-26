# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        return solve2(root,targetSum)
    
def solve(root, targ):
    if root is None: return False
    
    def run(node):
    

        if (node.left is None) and (node.right is None ):
            return [node.val]
        
        left = []
        if node.left is not None:
            left = run(node.left)
        right = []
        if node.right is not None:
            right = run(node.right)

        
        #left.extend(right)
        left = left + right
        for i in range(len(left)):
            left[i] += node.val
        return left
        

    mass = run(root)

    for el in mass:
        if el == targ:
            return True
    return False


def solve2(root, targ):

    if root is None: return False
    if root.left is None and root.right is None:
        return targ == root.val
    
    temp = targ - root.val

    return solve2(root.left, temp) or solve2(root.right, temp)
