---
title: "BinarySearchTree" # 타이틀 
author: "yongbeomkwak" #  작성자 
date: 2022-04-26 18:00 +09:00 # 날짜  
categories: [DataStructure,Tree,BinarySearchTree] #카데고리 
tags: [Python] #테그 
use_math: true #수식 사용

---

## 이진탐색트리란?


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
    
    def getLeft(self) -> Anode:
        if(self.left!=None):
            return self.left
        return None
    
    def getRight(self) -> Anode:
        if(self.right!=None):
            return self.right
        return None
    
    
    def isLeaf(self) -> bool:
        if(self.left==None and self.right==None): #자식노드가 모두 없으면 True
            return True
        return False
    
    def setRight(self,n:Anode):
        self.right=n
    
    def setLeft(self,n:Anode):
        self.left=n
~~~

<br>

### Dictionary(Dictionary.py)
~~~python
from typing import TypeVar
from abc import *

E = TypeVar('E')
K = TypeVar('K')

class Dictionary(metaclass=ABCMeta):

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def insert(self,key:K,e:E):
        pass

    @abstractmethod
    def remove(self,key:K)-> E:
        pass

    @abstractmethod
    def removeAny(self) -> E:
        pass

    @abstractmethod
    def find(self,key:K)->E:
        pass

    @abstractmethod
    def size(self)->int:
        pass
~~~


<br>

### BST(BST.py)

~~~python
from Dictionary import *
from Node import *
from typing import TypeVar
E = TypeVar('E')
K = TypeVar('K')

class BST(Dictionary):
    
    def __init__(self):
        self.root:Node=None
        self.__size:int=0



    def size(self) -> int:
        return self.__size
    
    def clear(self):
        self.root=None
        self.__size=0

    
    def insert(self, key: K, e: E):
        if(self.root==None): # 최상위가 비어있으면 설정
            self.root=Node(self.Entry(key,e),None,None)
        else:
            self.insert_helper(key,e,self.root)
        
        self.__size+=1
        
    
    def insert_helper(self,key:K,e:E,rt:Node)->Node:
        
        if(rt==None):
            return Node(self.Entry(key,e),None,None)
        elif(rt.getItem().key==key):
            self.rt.getItem().element=e
        elif(rt.getItem().key<key): #현재키가  목표보다 작으면 오른쪽으로
            rt.setRight(self.insert_helper(key,e,rt.getRight()))
        else: 
            rt.setLeft(self.insert_helper(key,e,rt.getLeft()))

        return rt
        
    
    def remove(self, key: K) -> E:
        return super().remove(key)
    
    def removeAny(self) -> E:
        return super().removeAny()
    
    def find(self, key: K) -> E:

        return self.find_helper(key,self.root)
        
    
    def find_helper(self,k:K,rt:Node) -> E:
        
        if(rt==None): #못 찾았을 때
            return None
        
        if(rt.getItem().key==k):
            return (rt.getItem().element)
        
        elif(rt.getItem().key<k): #현재보다 높은 값이면 오른쪽
            return self.find_helper(k,rt.getRight())

        else: #작으면 왼쪽
            return self.find_helper(k,rt.getLeft())
        

    class Entry:
        
        def __init__(self,key:K,e:E):
            self.key:K=key
            self.element:E=e
        
~~~

<br>

### 테스트(testAll.py)

~~~python
from BST import *
if __name__=="__main__":

    bst:Dictionary=BST()

    bst.insert(11,"a")
    bst.insert(3,"b")
    bst.insert(5,"c")
    bst.insert(2,"d")
    

    print(bst.find(2))  # d 
    print(bst.find(5))  # c
    print(bst.find(3))  # b 
    print(bst.find(11)) # a
    print(bst.find(30)) #None
~~~

