# -*- coding: utf-8 -*-
from abc import *
from typing import TypeVar
E = TypeVar('E')

class Anode(metaclass=ABCMeta):
    
    @abstractmethod
    def getItem(self) -> E:
        pass

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