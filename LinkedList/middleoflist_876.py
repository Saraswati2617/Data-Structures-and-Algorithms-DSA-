class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s=f=head
        while f and f.next:
            s=s.next
            f=f.next.next
        return s