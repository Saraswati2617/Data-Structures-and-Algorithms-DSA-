
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
    def reorderList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Find middle of the list
        s=f=head
        while f and f.next:
            p=s
            s=s.next
            f=f.next.next
        print(p.val)
        
        # reverse the second half
        new_h=s
        while s:
            pass
            
            



l1=buildLinkedList([1,2,3,4,5])
sol=Solution()
res=sol.reorderList(l1)
printLinkedList(res)



        




