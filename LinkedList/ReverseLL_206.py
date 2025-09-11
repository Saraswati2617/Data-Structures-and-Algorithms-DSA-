
from typing import List
from typing import Optional
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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        temp1=None
        temp2=None
        while curr:
            temp2=curr.next
            curr.next=temp1
            temp1=curr
            curr=temp2
            
        return temp1

l1=buildLinkedList([1,2,3,4,5])
# l2=buildLinkedList([9,9,9,9])
sol=Solution()
res=sol.reverseList(l1)
printLinkedList(res)



        




