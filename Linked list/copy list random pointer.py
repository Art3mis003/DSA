class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class solution:
    def deepcopy(self,head):
        copy={None:None}
        curr=head
        while curr:
            temp=Node(curr.val)
            copy[curr]=temp.val
            curr=curr.next
        curr=head
        while curr:
            temp=copy[curr]
            temp.next=copy[curr.next]
            temp.random=copy[curr.random]
            curr=curr.next
        return copy[head]


