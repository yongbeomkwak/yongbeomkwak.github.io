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