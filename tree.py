class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def preorder(root):
    if root==None:
        return
    else:
        print(root.val)
        preorder(root.left)
        preorder(root.right)
    
def inorder(root):
    if root==None:
        return
    else:
        inorder(root.left)
        print(root.val)
        inorder(root.right) 
        
def postorder(root):
    if root==None:
        return
    else:
        postorder(root.left)
        postorder(root.right)
        print(root.val)

def main():
    root=Node(500)
    First=Node(250)
    Second=Node(700)
    Third=Node(400)
    Fourth=Node(600)
    Fifth=Node(100)
    Sixth=Node(800)
    root.left=First
    root.right=Second
    First.right=Third
    First.left=Fifth
    Second.left=Fourth
    Second.right=Sixth
    print("Preorder:")
    preorder(root)
    print("Inorder:")
    inorder(root)
    print("Postorder:")
    postorder(root)

if __name__=="__main__":
    main()