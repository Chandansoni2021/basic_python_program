# how to initialize elements in a tree DSA in python
class BST():
    def __init__(self,key):
        self.key= key
        self.lchild=None
        self.rchild=None
    def insert(self,data):
        if self.key is None:
            self.key=data
            return
        if self.key>data:
            if self.child:
                self.lchild.insert(data)
            else:
                self.lchild=BST(data)
        
        else:
            if self.rchild:
                    self.rchild.insert(data)
            else:
                self.rchild=BST(data)
root=BST(10)
lst=[10,20,30,14,2]
for i in lst:
    root.insert(i)


    