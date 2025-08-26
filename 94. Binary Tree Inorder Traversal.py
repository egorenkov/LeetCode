# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        seq = []
        def run(node, arr):
            if not node: return 

            run(node.left, arr)
            arr.append(node.val)
            run(node.right, arr)
        
        run(root,seq)
        return seq
