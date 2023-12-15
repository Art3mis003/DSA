class ListNode:
    pass


class solution:
    def removeN(head,n):
        dummy= ListNode(0,head)
        left=dummy
        right=head
        while right and n>0:
            right=right.next
            n-=1
        while right:
            right=right.next
            left=left.next
        left.next=left.next.next
        return dummy.next
