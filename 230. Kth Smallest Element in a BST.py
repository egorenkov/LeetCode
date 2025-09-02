# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        #return brute_force(root,k)
        #return opt_brute_force(root,k)
        return solve(root,k)


def brute_force(root,k):

    def take_arr(node, arr):
        if node is None: return 
        arr.append(node.val)
        take_arr(node.left, arr)
        take_arr(node.right, arr)
    
    seq = []
    take_arr(root, seq)

    seq.sort()
    return seq[k -1]



def opt_brute_force(root,k):

    def take_arr(node, arr):
        if node is None: return 
        arr.append(node.val)
        take_arr(node.left, arr)
        take_arr(node.right, arr)


    def k_por(arr, k):
        if k<0 or k >= len(arr): return -1

        pivot = arr[len(arr) // 2]
        left = [el for el in arr if el < pivot]
        right = [el for el in arr if el > pivot]
        equal = [el for el in arr if el == pivot]

        if k < len(left):
            return k_por(left,k)
        
        elif k < len(left) + len(equal):  # Исправлено условие
            return pivot
        else:
            return k_por(right, k - len(left) - len(equal))




    seq = []
    take_arr(root, seq)



    return k_por(seq,k-1)


def solve(root,k):

    stack = []

    while root or stack:

        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()
        k -= 1
        if k == 0:
            return root.val
        
        root = root.right

    return -1
