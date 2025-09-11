class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        d=ListNode()
        d.next=head
        A=B=d
        for i in range(n+1):
            A=A.next
        while A:
            A=A.next
            B=B.next
        B.next=B.next.next

        return d.next