from Node import *

""" File containing methods for creating and manipulating 
	trees
"""

def createTreeGini(node):
	children = node.createChildrenGini()
	for child in children:
		#if examples empty, return parent plurality value
		if(child.examplesEmpty()):
			continue
		#if labels empty return child plurality value
		elif(child.attributesEmpty()):
			continue
		#if we can determine yes or no
		elif(child.isYes() or child.isNo()):
			continue
		else:
			createTreeGini(child)
def createTreeInfo(node):
	children = node.createChildrenInfo()
	for child in children:
		if(child.examplesEmpty()):
			continue
		#if labels empty return child plurality value
		elif(child.attributesEmpty()):
			continue
		#if we can determine yes or no
		elif(child.isYes() or child.isNo()):
			continue
		else:
			createTreeInfo(child)

""" Begin utility functions for trees """
def traverseTree(root):
	print root.toString()
	children = root.getChildren()
	for child in children:
		traverseTree(child)
""" Creates a list of tuples, each corresponding to
	a an example, label pair """
def createCounter(examples, labels):
	newList = []
	i = 0
	for example in examples:
		newList.append((example,labels[i]))
		i+=1
	return newList

def compareTree(root1, root2):
	#if we did not split by the same attrnum
	if root1.getAttrNum() != root2.getAttrNum():
		return False
	elif root1.getCounter() != root2.getCounter():
		return False
	else:
		return compareChildren(root1, root2)

def compareChildren(root1, root2):
	print "Comparing nodes ",root1," and ",root2
	if root1.getAttrNum() != root2.getAttrNum():
		print "Nodes were split by separate attribute numbers"
		return False
	if root2.getCounter() != root2.getCounter():
		print "Nodes do not have the same counter"
		return False
	#if netheir root has children, and the counters and attrnum are the same
	#we can return true
	if not root1.getChildren() and not root2.getChildren():
		print "Nodes are leaf nodes with no children"
		print "Node 1 counter \n",root1.toString()
		print "Node 2 counter \n",root2.toString()
		return True
	print "Node 1 counter \n",root1.toString()
	print "Node 2 counter \n",root2.toString()
	print "Creating children from (rel) attrnum - ",root1.getAttrNum()
	return compareChildren(root1.getChildren()[0],root2.getChildren()[0]) and compareChildren(root1.getChildren()[1],root2.getChildren()[1])