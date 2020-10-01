#!/usr/bin/python3

import random

class Node:
    def __init__(self,value):
        self.left=None
        self.right=None
        self.value=value
    def insert(self,guest):
        if guest<self.value:
            if self.left==None:
                self.left=Node(guest)
            else:
                self.left.insert(guest)
        elif guest>self.value:
            if self.right==None:
                self.right=Node(guest)
            else:
                self.right.insert(guest)
    def display_inorder(self):
        if self.left!=None:
            self.left.display_inorder()
        print(self.value)
        if self.right!=None:
            self.right.display_inorder()
    def preorder(self):
        print(self.value)
        if self.left!=None:
            self.left.preorder()
        if self.right!=None:
            self.right.preorder()
    def postorder(self):
        if self.left!=None:
            self.left.postorder()
        if self.right!=None:
            self.right.postorder()
        print(self.value)

def main():
    obj=Node(40)
    for i in range(0,10):
        r=random.randint(10,80)
        obj.insert(r)
    print("Inorder:{}".format(obj.display_inorder()))
    print("Preorder:{}".format(obj.preorder()))
    print("Postorder:{}".format(obj.postorder()))

if __name__=='__main__':
    main()
