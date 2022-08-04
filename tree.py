class treenode:
    def __init__(self, root, child=[]):
        self.root=root
        self.child=child
    def __str__(self,leval=0):
        ret=" "*leval+str(self.root)+"\n"
        for child in self.child:
            ret += child.__str__(leval+1)
        return ret
    def add(self, treenode):
        self.child.append(treenode)
root=treenode("drinks",[])
cold=treenode("cold",[])
hot=treenode("hot",[])
root.add(cold)
root.add(hot)
cola=treenode("cola",[])
fanta=treenode("fanta",[])
cold.add(cola)
cold.add(fanta)
cofee=treenode("cofee",[])
tea=treenode("tea",[])
hot.add(cofee)
hot.add(tea)
print(root)