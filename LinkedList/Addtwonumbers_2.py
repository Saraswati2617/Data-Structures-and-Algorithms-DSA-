
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def buildLinkedList(value:List[int]):
    dummy = ListNode()
    curr = dummy
    for v in value:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def printLinkedList(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(result)


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry
            carry = total // 10
            curr.next = ListNode(total % 10)

            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next

l1=buildLinkedList([9,9,9,9,9,9,9])
l2=buildLinkedList([9,9,9,9])
sol=Solution()
res=sol.addTwoNumbers(l1,l2)
printLinkedList(res)



        




