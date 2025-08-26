# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def make_array(node):

            arr = []

            while node:
                arr.append(node.val)
                node = node.next
            return arr
        
        if not head:
            return None
        arr = make_array(head)
        
        arr.sort()
        dummy = ListNode(0)
        new_head = ListNode(arr[0])
        dummy.next = new_head

        for i in range(1,len(arr)):
            new_head.next = ListNode(arr[i])
            new_head = new_head.next

        return dummy.next
