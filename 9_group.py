#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#这是做了一个简单例子，完成了符合要求的类和函数。因为赶时间没有做供用户手动创建节点,手动增加节点，手动获得叶子节点，手动输出树的结构等交互式界面，我会在写完第四个题目以后增加这些的。
import time
class Node():
    uniq_num=0 #set a static value  everyleaf's number 
    def __init__(self,data=None):
        self.data=data
        self.child=[]
        self.father=None
        Node.uniq_num+=1
        self.uniq_num=Node.uniq_num
    def __str__(self):
        return self.uniq_num
    
class Tree():
    def __init__(self):
        self.all_leaf=[]
        self.depth=0
    def add(self,ftree,ctree):#add node
        if ctree.father==None:#not has father node,add it 
            ftree.child.append(ctree)
            ctree.father=ftree
        else:
            print("error[1]:this child has father")
    def get(self,tree):# get leaf node
        length=len(tree.child) #set chlid number
        if length==0: # when is a leaf node
            info=(tree.uniq_num,tree.data)
            self.all_leaf.append(info)
        else:
            for i in range(length): # Recursive
                self.get(tree.child[i])
        return self.all_leaf
    def leaf_clear(self):# clear all_leaf
        self.all_leaf=[]
    def find_depth(self,tree):#find this child tree's depth
        if tree.father!=None:
            self.depth+=1
            self.find_depth(tree.father)
        
    def printf(self,tree):#print schema of this child tree
        self.depth_clear()
        flag=" "
        self.find_depth(tree)
        print("%s-%d" % (flag*self.depth,tree.uniq_num))
        length=len(tree.child) #set chlid number
        for i in range(length): # Recursive
            self.printf(tree.child[i])
    def depth_clear(self):# clear depth
        self.depth=0
        
#simple demo:
root=Tree()
node1=Node("1");node2=Node("2")
node3=Node("3");node4=Node("4")
node5=Node("5");node6=Node("6")
node7=Node("7");node8=Node("8")
print("    1.adding node")
root.add(node1,node2);print("add(node1,node2) successful");time.sleep(1);
root.add(node1,node4);print("add(node1,node4) successful");time.sleep(1);
root.add(node1,node6);print("add(node1,node6) successful");time.sleep(1);
root.add(node4,node3);print("add(node4,node3) successful");time.sleep(1);
root.add(node4,node5);print("add(node4,node5) successful");time.sleep(1);
root.add(node3,node7);print("add(node3,node7) successful");time.sleep(1);
root.add(node3,node8);print("add(node3,node8) successful\n");time.sleep(1);
print("    2.get leaf ,demo node is root(node1):")
print(root.get(node1));root.leaf_clear()
time.sleep(1)
print("\n    3.the Tree's schema :")
root.printf(node1);
