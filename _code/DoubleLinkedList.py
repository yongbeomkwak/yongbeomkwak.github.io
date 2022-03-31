# -*- coding: utf-8 -*-
from typing import TypeVar
from Dlink import *
from List import *
from ListIterator import *

E = TypeVar('E')

class DoubleLinkedList(List):
    def __init__(self) -> None:
        self.head:Dlink=Dlink(None,None,None)
        self.tail=self.head
        self.size=0
    
    def insert(self,pos: int, item: E):
        curr:Dlink=self.head
        
        for _ in range(pos):
            curr=curr.next 
        
        new:Dlink=Dlink(item,curr,curr.next)
        curr.next=new

        if(curr==self.tail):
            self.tail=curr.next
        
        self.size+=1
    
    def length(self) -> int:
        return self.size
    
    def append(self, item: E):
        
        new:Dlink=Dlink(item,self.tail,None)
        self.tail.next=new
        self.tail=new
    
    def clear(self):
        self.head=None
        self.tail=None
        self.size=0
    
    def update(self, pos: int, item: E):
        curr:Dlink=self.head

        for _ in range(pos):
            curr=curr.next
        
        curr.item=item
    
    def getValue(self, pos: int):
        curr:Dlink=self.head

        for _ in range(0,pos): # 탐색
            curr=curr.next
        return curr.next.item
    
    def remove(self, pos: int):
        return super().remove(pos)

        

    
    def listIterator(self) -> ListIterator:
        return self.DoubleLinkedListIterator(self)

    
    class DoubleLinkedListIterator(ListIterator):
        
        def __init__(self,outer):
            self.outer:DoubleLinkedList=outer
            self.curr:Dlink=self.outer.head
        
        def hasNext(self) -> bool:
            return self.curr!=self.outer.tail
        
        def next(self) -> E:
            self.curr=self.curr.next
            return self.curr.item
        
        
        

