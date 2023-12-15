def CycleIn(head):
    slow,fast=head,head
    while fast and fast.next:
        slow=head.next
        fast=head.next.next
        if slow==fast:
            return True
    return False

def hasCycle(head):
    hash = set()
    temp = head
    while temp and temp.next:
        hash.add(temp)
        temp = temp.next
        if temp in hash:
            return True
    return False