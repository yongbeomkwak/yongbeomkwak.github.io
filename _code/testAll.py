from BST import *
if __name__=="__main__":

    bst:Dictionary=BST()

    bst.insert(11,"a")
    bst.insert(3,"b")
    bst.insert(5,"c")
    bst.insert(2,"d")
    

    print(bst.find(2))  # d 
    print(bst.find(5))  # c
    print(bst.find(3))  # b 
    print(bst.find(11)) # a
    print(bst.find(30)) #None
  