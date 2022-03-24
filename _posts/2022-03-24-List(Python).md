---
title: "배열 기반 리스트(데이터구조)[1]" # 타이틀 
author: "yongbeomkwak" #  작성자 
date: 2022-03-24 13:35 +09:00 # 날짜  
categories: [DataStructure] #카데고리 
tags: [List,Python] #테그 
use_math: true #수식 사용

---

### 리스트란?

<br>

<img src="https://user-images.githubusercontent.com/48616183/159843269-197877bc-1280-41a4-a167-5bc1c0ba7934.png" height="70%" width="70%">




<br>

### List구조의 ADT
ADT: Abstract Data Type

Java의 인터페이스 역할

<br>

<img src="https://user-images.githubusercontent.com/48616183/159843994-cdea2f60-70b6-40c0-84f2-749bc76cba41.png" height="70%" width="70%">


<br>


-   ADT(List.py)

<br>

~~~ python

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

~~~

<br>

>   insert와 remove는 pos변수를 사용하므로 아래 그림으로 반복문 연산을 이해

<br>

#### _insert_
![insert](https://user-images.githubusercontent.com/48616183/159891442-35ef02b6-5a27-428c-a769-bc916b21c338.png)

<br>

#### _remove_

![remove](https://user-images.githubusercontent.com/48616183/159891668-4218bb0c-33ec-4678-b5d5-9bae49792c22.png)

<br>

<br>
<br>
<br>
<br>
<br>

-   ArrayList(ArrayList.py)

<br>

~~~ python

# -*- coding: utf-8 -*-

from List import *
import numpy as np


class ArrayList(List):
    DefaultSize=10
    data=None

    def __init__(self,size=DefaultSize):
        ArrayList.data=np.zeros(size)
        self.listSize=0
    #클래스 메서드(class method)란 객체가 아닌 클래스 자체에 묶여있는(bound to) 메서드이다. 
    # 또다른 생성자 선언
    @classmethod
    def from_size(cls,size):
 
        ArrayList.data=np.zeros(size)       
        return cls(size)  #cls로  __init__으로 넘겨준 후 리턴
    
    def length(self):
        return self.listSize

    def clear(self):
        self.listSize=0
    
    def update(self,pos,item):
        ArrayList.data[pos]=item
    
    def getValue(self,pos):
        return ArrayList[pos]
    
    def append(self,item):
        ArrayList.data[self.listSize]=item
        self.listSize+=1
    
    def insert(self,pos,item):
        # 끝에부터 포스 앞까지 뒤로 당김
        for i in range (self.listSize,pos,-1):
            
            ArrayList.data[i]=ArrayList.data[i-1]

        ArrayList.data[pos]=item
        self.listSize+=1

    def remove(self,pos):
        ret=ArrayList.data[pos]

        
        # 왼쪽으로 옮기기 
        for i in range(pos,self.listSize):
            ArrayList.data[i]=ArrayList.data[i+1]

        self.listSize-=1 #사이즈 감소


        return ret
~~~

-   실제 구현동작 확인(test.py)

~~~ python
from ArrayList import *

if __name__=="__main__":

    mylist=ArrayList()
    mylist.append(3)
    print(mylist.data)
    mylist.append(5)
    print(mylist.data)

    mylist.insert(0,10)
    print(mylist.data)


    mylist.remove(2)
    print(mylist.data)
    print(mylist.length())

    mylist2=ArrayList(30)
    print(mylist2.data)

~~~

-   결과

![result](https://user-images.githubusercontent.com/48616183/159893084-87709bb4-6835-4c4e-bd3c-2e24b7a4c69b.png)

<br>

- 배열기반 리스트의 한계

<br>

![한계](https://user-images.githubusercontent.com/48616183/159893232-9ed0a649-2840-467e-ba27-dd471a343056.png)



  