---
title: "Tree" # 타이틀 
author: "yongbeomkwak" #  작성자 
date: 2022-04-12 15:00 +09:00 # 날짜  
categories: [DataStructure,Tree,ArrayTree] #카데고리 
tags: [Python] #테그 
use_math: true #수식 사용

---

## 배열기반 트리란?

<br>

<img src="https://user-images.githubusercontent.com/48616183/162893123-68339544-1b36-41c3-852c-ebcabcc9daac.png" height="70%" width="70%">


-   배열기반 트리 제약조건
    - Complete Binary Tree
    - 해당 인덱스가 범위를 벗어났는지 또는 다른 조건을 만족하는지 선행체크


<br>


~~~ python
import math
class ArrayTree:
    
    def __init__(self) -> None:
        self.tree=['A','B','C','D','E','F','G','H','I','J','K','L']
        self.size:int=len(self.tree)
    
    def parent(self,curr:int): # 해당 curr의 부모 찾기
        if(curr>0):
            return self.tree[math.floor((curr-1)/2)]
        else : 
            return "It is root"
    
    def leftchild(self,curr:int):
        #left=2n+1
        if(2*curr+1<self.size):
            return self.tree[2*curr+1]
        else:
            return "No left Child"
    
    def rightchild(self,curr:int):
        #right=2n+2
        if(2*curr+2<self.size):
            return self.tree[2*curr+2]
        else:
            return "No right Child"

    def leftSibling(self,curr):
        #left Sibling=n-1
        if(curr%2==0):
            return self.tree[curr-1]
        
        return "No left Sibling"
    
    def rightSibling(self,curr):
        #right sibling=n+1

        if(curr%2!=0 and curr+1<self.size):
            return self.tree[curr+1]

        return "No right Sibling" 

    


~~~

