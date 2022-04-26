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
        
            
