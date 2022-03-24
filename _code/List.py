# -*- coding: utf-8 -*-
from abc import *


class List(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def clear(self):
        pass
    
    @abstractmethod
    def insert(self,pos,item):
        pass

    @abstractmethod
    def append(self,item):
        pass

    @abstractmethod
    def update(self,pos,item):
        pass
    
    @abstractmethod
    def getValue(self,pos):
        pass
    
    @abstractmethod
    def remove(self,pos):
        pass

    @abstractmethod
    def length(self) : 
        pass