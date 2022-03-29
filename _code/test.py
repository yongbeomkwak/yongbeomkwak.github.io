from ArrayList import *
from LinkedList import *

if __name__=="__main__":

    myList=LinkedList()
    myList.append(3)
    print(myList.toString())
    myList.insert(0,1)
    print(myList.toString())
    myList.insert(0,4)
    print(myList.toString())
    myList.append(10)
    print(myList.toString())
    myList.insert(1,5)
    print(myList.toString())
    print("Remove value: ",myList.remove(1))
    print(myList.toString())
    print("Length: ",myList.length())