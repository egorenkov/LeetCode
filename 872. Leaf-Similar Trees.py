# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def LeafArr(self, root, arr):
        
        if root.left is None and root.right is None:
            arr.append(root.val)
            return 
        
        if root.left is not None:
            self.LeafArr(root.left, arr)
            
        if root.right is not None:
            self.LeafArr(root.right, arr)
            
        return 
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        ans_arr1 =[]
        self.LeafArr(root1,ans_arr1)

        ans_arr2 = []
        self.LeafArr(root2, ans_arr2)
        
        if len(ans_arr1) != len(ans_arr2):
            return False
        for i in range(len(ans_arr1)):
            if ans_arr1[i] != ans_arr2[i]:
                return False
        return True
