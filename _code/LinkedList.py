# -*- coding: utf-8 -*-

from List import *
from Link import *

class LinkedList(List):

    def __init__(self):
        self.head:Link=Link(None,None)
        self.tail=self.head #초기화 이므로 같은 head와 tail 같게
        self.size:int=0
    
    def clear(self):
        self.head=None
        self.tail=None
        self.size=0
    
    def insert(self, pos: int, item: E):
        curr:Link=self.head
        for i in range(0,pos):
            curr=curr.next
        

        # 1(새 노드)        
        # 0(현재노드) -> 2(햔재노드 다음)

        #new_node:Link=Link(item=item,next=curr.next)      1 -> 2
        #curr.next=new_node  0->1
        # 0->1->2

        #새 노드의 다음 노드를 현재노드의 다음으로 지정
        new_node:Link=Link(item=item,next=curr.next)
        #햔재노드의 다음을 새노드로 지정 
        curr.next=new_node

        if(curr==self.tail): #만약 현재 노드가 tail이면 
            self.tail=curr.next #tail 수정 
        self.size+=1

    def append(self,item:E):
        new_node:Link=Link(item=item,next=None)
        self.tail.next=new_node
        self.tail=new_node
        self.size+=1

    def update(self, pos: int, item: E):
        curr:List=self.head

        for i in range(0,pos): # 탐색
            curr=curr.next
        
        curr.next.item=item # 업데이트 
    
    def getValue(self, pos: int)-> E:
        curr:List=self.head

        for i in range(0,pos): # 탐색
            curr=curr.next

        return curr.next.item

    def length(self) -> int:
        return self.size
    
    def remove(self, pos: int) -> E:
        curr:List=self.head

        for i in range(0,pos): # 탐색
            curr=curr.next
        
        #curr.next가 삭제해야할 노드 
        ret:E=curr.next.item

        if(curr.next==self.tail): #만약 삭제해야할 노드가 tail이면
            self.tail=curr  # tail 옮김 

        curr.next=curr.next.next # 다다음 것으로 옮긴다.
        
        self.size-=1


        return ret

    
    def toString(self) -> str:
        ret:str=""
        curr:Link=self.head

        for i in range(0,self.size):
       
            ret+= str(curr.next.item) + ","
            curr=curr.next

        
        return ret

    