# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        def convert(list):
            num = ''
            while list != None:
                num = str(list.val) + num
                list = list.next
            return int(num)

        num1, num2 = convert(l1), convert(l2)
        num = num1 + num2

        root = ListNode(num%10)
        l3 = root
        num = num // 10
        while num != 0:
            l3.next = ListNode(num%10)
            l3 = l3.next
            num = num // 10

        return root
