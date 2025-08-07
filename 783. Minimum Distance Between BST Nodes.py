# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def dfs(self, node, arr):
        arr.append(node.val)
        if node.left is None and node.right is None:
            return 
        
        if node.left is not None:
            self.dfs(node.left, arr)
            
        if node.right is not None:
            self.dfs(node.right, arr)
           

    def minDiffInBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        ans = []
        self.dfs(root, ans)
        ans.sort()
        mini = abs(ans[0] - ans[1])
        for i in range(1, len(ans) -1):
            if mini > abs(ans[i]-  ans[i + 1]):
                mini = abs(ans[i]- ans[i + 1])

        return mini
