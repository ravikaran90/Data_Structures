class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

def display(head):
    current=head
    while current:
        print("Value:",current.val)
        current=current.next

def middleoflinkedlist(head):
    slow=fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    return slow.val

def ifcycle(head):
    slow=fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            return True
    return False

def reversal(head):
    current=head
    prev=None
    while current:
        temp=current.next
        current.next=prev
        prev=current
        current=temp
    return prev

def main():
    head=Node(100)
    Second=Node(200)
    Third=Node(300)
    Fourth=Node(400)
    Fifth=Node(500)
    head.next=Second
    Second.next=Third
    Third.next=Fourth
    Fourth.next=Fifth
    display(head)
    mid=middleoflinkedlist(head)
    print("Middle Value:",mid)
    newhead=reversal(head)
    display(newhead)
    res=ifcycle(head)
    print("If Cycle Exists:",res)

if __name__=="__main__":
    main()