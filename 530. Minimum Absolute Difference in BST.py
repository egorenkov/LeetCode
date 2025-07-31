# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def dfs(self, root,arr):
        if root is None:
            return
        arr.append(root.val)
        self.dfs(root.left,arr)
        self.dfs(root.right,arr)


    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        arr = []
        self.dfs(root,arr)
        arr.sort()
        r = float('inf')
        for i in range(len(arr)-1):
            r = min(r, arr[i+1] - arr[i])
        return r
