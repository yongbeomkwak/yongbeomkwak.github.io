from Heap import *
if __name__=="__main__":

    arr=[1,2,3,4,5]
    heap=MaxHeap(arr,len(arr),20)
    heap.insert(100)
    heap.insert(1000)
    heap.insert(0)
   
    heap.prt()
    while(not(heap.isempty())):
        print(heap.removemax())
    