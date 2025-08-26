# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None

        curr = head

        while curr:
            if curr.next and curr.val == curr.next.val:
                new_curr = curr.next
                while new_curr and new_curr.val == curr.val:
                    new_curr = new_curr.next
                
                curr.next = new_curr
            curr = curr.next

        return head
