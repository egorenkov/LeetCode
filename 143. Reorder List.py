# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """

        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        curr = slow

        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        first, second = head, prev
        while second.next:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

        """
        if head is None:
            return None 

        def find_arr(node):
            res = []
            curr = node
            while curr:
                res.append(curr.val)
                curr = curr.next
            return res
        arr = find_arr(head)

        dummy = ListNode(0)
        new_head = ListNode(arr[0])
        dummy.next = new_head
        
        
        l = 1
        r = len(arr) - 1
        while l < r:
            new_head.next = ListNode(arr[r])
            new_head = new_head.next
            new_head.next = ListNode(arr[l])
            new_head = new_head.next
            
            l += 1
            r -= 1
        
        if len(arr) %2 == 0:
            new_head.next = ListNode(arr[l])


        head = dummy.next
        """
