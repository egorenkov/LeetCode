# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def Perebor(self, node, arr):
        arr.append(node.val)
        if node.next is None:
            return
        else:
            self.Perebor(node.next, arr)
            return

    def Create(self, arr):
        if len(arr) <= 1:
            if len(arr) == 1:
                return ListNode(arr[0])
            else:
                return None

        res = ListNode(arr[0])
        temp = ListNode()
        res.next = temp
        for el in range(1, len(arr) - 1):
            temp.val = arr[el]
            
            temp.next = ListNode()
            temp = temp.next

        temp.val = arr[len(arr)- 1]
        return res

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        arr_l1 = []
        self.Perebor(l1,arr_l1)
        arr_l2 = []
        self.Perebor(l2,arr_l2)

        int_l1 = int("".join(list(map(str, arr_l1[::-1]))))
        int_l2 = int("".join(list(map(str, arr_l2[::-1]))))

        r = int_l1 + int_l2
        arr = []
        if r == 0:
            return self.Create([0])
        while r >0 :
            arr.append(r % 10)
            r = r//10
        

        return self.Create(arr)


