from Sorting import *
if __name__=="__main__":
    
    a=[i for i in range(30,-1,-1)]
    s=Sorting(a)
    
    print(s.insertionSort())
    print(s.bubbleSort())
    print(s.selectionSort())
    print(s.shellSort())
    s.view()
