def recurReverseList(head):
    if not head :
        return None
    newhead= head
    if head.next:
        newhead=recurReverseList(head.next)
        head.next.next=head
        head.next=None
    return newhead  
