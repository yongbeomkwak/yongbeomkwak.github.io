from BST import *
if __name__=="__main__":

    bst:Dictionary=BST()
    bst.insert(10,"a")
    bst.insert(9,"b")
    bst.insert(15,"c")
    bst.insert(5,"d")
    bst.insert(13,"e")
    bst.insert(18,"f")
    bst.insert(11,"g")
    bst.insert(12,"h")
    bst.insert(14,"i")
    bst.insert(20,"k")
    bst.inorder(bst.root)
  