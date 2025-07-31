# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def Descent(self,node,strr,arr):

        if node.left is None and node.right is None:
            arr.append(strr + str(node.val))
            return

        if node.left is not None and node.right is not None :
            strr= strr + str(node.val)
            self.Descent(node.left,strr,arr)
            self.Descent(node.right, strr , arr)
            return
        elif node.left is None and node.right is not None :
            self.Descent(node.right, strr + str(node.val),arr)
            return
        else:
            self.Descent(node.left,strr + str(node.val), arr)
            return
       

    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        arr = []

        self.Descent(root,"", arr)

        return sum(list(map(int , arr)))
        
