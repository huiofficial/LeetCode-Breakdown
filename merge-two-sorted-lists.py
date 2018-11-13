# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None

        l = ListNode(None)
        head = l

        while l1!=None and l2!=None:
            if l1.val < l2.val:
                l.val = l1.val
                l.next = l1.next
                l1 = l1.next
            else:
                l.val = l2.val
                l.next = l2.next
                l2 = l2.next
            if l1!=None or l2!=None:
                l.next = ListNode(None)
                l = l.next
                # print("1")

        while l1!=None:
            l.val = l1.val
            l.next = l1.next
            l1 = l1.next
            if l1!=None:
                l.next = ListNode(None)
                l = l.next
                # print("2")

        while l2!=None:
            l.val = l2.val
            l.next = l2.next
            l2 = l2.next
            if l2!=None:
                l.next = ListNode(None)
                l = l.next
                # print("3")

        return head

            
