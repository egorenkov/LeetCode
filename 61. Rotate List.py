# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

        
        arr = []
        
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        dummy = ListNode(0)

        N = len(arr)
        if N == 0:
            return None
        i = (N - k) %N
        new_head = ListNode(arr[i])
        dummy.next = new_head
        for j in range(N - 1):
                
            i = (i + 1) %N
            new_head.next = ListNode(arr[i])
            new_head = new_head.next
        return dummy.next
        
