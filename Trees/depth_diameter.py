class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def depth(root):
    if root==None:
        return 0
    else:
        leftst=depth(root.left)
        rightst=depth(root.right)
        return 1+max(leftst,rightst)

def diameter(root):
    return depth(root.left)+depth(root.right)

def main():
    root=Node(50)
    First=Node(25)
    Second=Node(75)
    Third=Node(30)
    Fourth=Node(100)
    root.left=First
    First.right=Third
    root.right=Second
    Second.right=Fourth
    dep=depth(root)
    print("Depth:",dep)
    diam=diameter(root)
    print("Diameter:",diam)

if __name__=="__main__":
    main()