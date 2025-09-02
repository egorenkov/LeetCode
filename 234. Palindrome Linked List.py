# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        rever, curr = None, slow
        while curr:
            temp = curr.next
            curr.next = rever
            rever = curr
            curr = temp

        head2 = head
        head3 = rever
        while head3:
            if head2.val != head3.val:
                return False
            head2 = head2.next
            head3 = head3.next
        return True


