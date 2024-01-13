# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # n are numbers, p are powers of 10
        n1 = 0
        p1 = 1
        n2 = 0
        p2 = 1

        while l1:
            n1 += l1.val * p1
            p1 = p1 * 10
            l1 = l1.next

        while l2:
            n2 += l2.val * p2
            p2 = p2 * 10
            l2 = l2.next

        ## reverse the string
        result = str(n1 + n2)[::-1]

        ## create the result linked list
        head = ListNode(result[0])
        current = head
        for i in range(1, len(result)):
            current.next = ListNode(result[i])
            current = current.next

        return head