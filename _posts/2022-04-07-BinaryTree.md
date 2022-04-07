---
title: "BinaryTree" # 타이틀 
author: "yongbeomkwak" #  작성자 
date: 2022-04-07 15:30 +09:00 # 날짜  
categories: [DataStructure,Tree,BinaryTree] #카데고리 
tags: [Python] #테그 
use_math: true #수식 사용

---

## 이진트리란?

<br>

<img src="https://user-images.githubusercontent.com/48616183/162139076-16837348-aa39-4dbd-96ac-b8ffb2a7c9b8.png" height="70%" width="70%">




<br>

## 이진트리 종류 
<br>

### Full Binary Tree , Complete Binary Tree

<br>

<img src="https://user-images.githubusercontent.com/48616183/162139315-b578f683-2d40-4662-ace5-ce912d3cbac0.png" height="70%" width="70%">

<br>

### Perfect Binary Tree

<br>


<img src="https://user-images.githubusercontent.com/48616183/162140958-6e61a3f6-2bbe-42e5-a398-737333961191.png" height="70%" width="70%">

<br>



## Binary Node ADT

<img src="https://user-images.githubusercontent.com/48616183/162141571-72bbe249-1b2b-4f20-a3e6-cf9d630ca3e3.png" height="70%" width="70%">


## 순회

<br>

<img src="https://user-images.githubusercontent.com/48616183/162141887-cf5c62fc-cfc1-4b25-8faa-13596a54088c.png" height="70%" width="70%">


## 코드
<br>

### ADT(Anode.py)
~~~python
# -*- coding: utf-8 -*-
from abc import *
from typing import TypeVar
E = TypeVar('E')

class Anode(metaclass=ABCMeta):
    
    @abstractmethod
    def getLeft(self)->E:
        pass
    
    @abstractmethod
    def getRight(self)->E:
        pass

    @abstractmethod
    def isLeaf(self)->bool:
        pass

    @abstractmethod
    def getItem(self)->E:
        pass

~~~

<br>


### Node(Node.py)

~~~python
from Anode import *
from typing import TypeVar
E = TypeVar('E')

class Node(Anode):
    def __init__(self,item:E,left:Anode=None,right:Anode=None):
        self.item:E=item
        self.left:Anode=left
        self.right:Anode=right

    def getItem(self) -> E:
        return self.item
    
    def getLeft(self) -> E:
        if(self.left!=None):
            return self.left.getItem()
        return "No item"
    
    def getRight(self) -> E:
        if(self.right!=None):
            return self.right.getItem()
        return "No item"
    
    
    def isLeaf(self) -> bool:
        if(self.left==None and self.right==None): #자식노드가 모두 없으면 True
            return True
        return False
~~~

<br>

### Tree(BinaryTree.py)
~~~python
from Node import *
from typing import TypeVar
E = TypeVar('E')

class BinaryTree:
    def __init__(self,root:Node):
        self.__root:Node=root
    
    def insert_Node(self,parent:Node,node:Node): #부모노드와 자식노드
        if(node.getItem()<parent.getItem()): # 부모보다 작으면 왼쪽
            if(parent.left==None): #비어있으면
                parent.left=node
                return
            else: #있다면 해당 왼쪽을 기준으로 재귀
                self.insert_Node(parent.left,node)
        else:
            if(parent.right==None):#비어있으면
                parent.right=node
                return
            else: #오른쪽으로 재귀
                self.insert_Node(parent.right,node)
    
    def getRoot(self)->Node:
        return self.__root

    def visit(self,node:Node):
        print(node.getItem())
    
    def preorder(self,node:Node):
        if(node==None):
            return
        self.visit(node) #자기자신
        self.preorder(node.left) #왼쪽 
        self.preorder(node.right) #오른쪽
    
    def postorder(self,node:Node):
        if(node==None):
            return
        self.postorder(node.left) #왼
        self.postorder(node.right) #오 
        self.visit(node) #자기자신 

    def inorder(self,node:Node):
        if(node==None):
            return
        self.inorder(node.left) #왼
        self.visit(node) #자기자신
        self.inorder(node.right) #오
~~~

<br>

### 테스트(testAll.py)

~~~python
from BinaryTree import *
from Node import *
if __name__=="__main__":
        root=Node(100)
    tree=BinaryTree(root)
    tree.insert_Node(root,Node(50))
    tree.insert_Node(root,Node(80))
    tree.insert_Node(root,Node(120))
    tree.insert_Node(root,Node(20))
    tree.insert_Node(root,Node(110))
    tree.insert_Node(root,Node(180))

    '''
                100
            50          120
        20      80   110    180
    '''

    print("Pre Order")
    tree.preorder(root)
    print("Post Order")
    tree.postorder(root)
    print("In Order")
    tree.inorder(root)
~~~

### 최종 구조
<br>
<img src="https://user-images.githubusercontent.com/48616183/162162395-16243649-4baf-4a6a-a8cb-82b4a93513a8.png" height="70%" width="70%">

<br>

### 결과

<br>

<img src="https://user-images.githubusercontent.com/48616183/162162614-fd16494f-fe50-4ee7-90a8-1bdaac51e1bb.png" height="70%" width="70%">

