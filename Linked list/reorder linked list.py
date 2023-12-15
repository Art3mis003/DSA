"""Could also be done using extra memory. by using
array and storing the nodes in it."""

def reorder(head):
    slow,fast=head,head.next
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    second= slow.next
    slow.next=None
    prev= None
    while second:
        nxt= second.next
        second.next=prev
        prev=second
        second=nxt
    first,second=head, prev
    while second:
        temp1,temp2=first.next,second.next
        first.next=second
        second.next=temp1
        first=temp1
        second=temp2

