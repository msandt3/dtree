import project4
import infogain
import util
from Node import *
import argparse
import gini


tryEx1 = [[1, 1, 0, 1, 1, 1, 1, 0],[1, 1, 1, 0, 1, 1, 1, 1],[1, 1, 0, 0, 0, 0, 0, 1]]
tryLa1 = [1,1,0]

""" Begin command line argument parsing """
parser = argparse.ArgumentParser()
parser.add_argument('testing', choices=['test1','test2','test3','test4'], help='data set to run testing on')
parser.add_argument('training', choices=['train1','train2','train3','train4'], help='data set to run training on')
parser.add_argument('method', choices=['infogain','gini'], help='select which learning method to use')


args = parser.parse_args()
testNum = args.testing[4]
trainNum = args.training[4]
method = args.method
""" End command line argument parsing """

""" Begin utility functions for trees """
def createTreeGini(node):
	children = node.createChildrenGini()
	for child in children:
		print "Child - ",child," \n",child.toString()
		#if examples empty, return parent plurality value
		if(child.examplesEmpty()):
			print "Examples empty"
		#if labels empty return child plurality value
		elif(child.attributesEmpty()):
			print "Attributes empty"
		#if we can determine yes or no
		elif(child.isYes() or child.isNo()):
			print "Yes or no decision"
			#return
		else:
			createTreeGini(child)
def createTreeInfo(node):
	children = node.createChildrenInfo()
	for child in children:
		if(child.examplesEmpty()):
			print "Examples empty"
		#if labels empty return child plurality value
		elif(child.attributesEmpty()):
			print "Attributes empty"
		#if we can determine yes or no
		elif(child.isYes() or child.isNo()):
			print "Yes or no decision"
		else:
			createTreeInfo(child)


def traverseTree(root):
	print "***** NODE ******\n"
	print root
	print "Parent: ",root.getParent()
	print "Attrnum: ",root.attrnum
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
def toString(dict):
	for item in dict:
		print item
def classifyList(examples, root):
	retlist = []
	for example in examples:
		retval = classifyExample(example,root)
		#retlist.append((example,retval))
		retlist.append(retval)
	return retlist

def classifyExample(example, root):
	#print root.toString()
	#print root.attrnum
	if(root.isYes()):
		return 1
	elif(root.isNo()):
		return 0
	#otherwise remove the attribute split by
	else:
		#print "Attribute number ",root.attrnum
		#print example
		attrval = example[root.attrnum]
		example.pop(root.attrnum)

		if attrval == 1:
			return classifyExample(example,root.getChildren()[0])
		else:
			return classifyExample(example,root.getChildren()[1])

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

def calculatePercentage(calcLabels,givenLabels):
	numCorrect = 0.0
	total = 0.0
	for i in range(0,len(calcLabels)):
		if calcLabels[i] == givenLabels[i]:
			numCorrect += 1
		total += 1
	return numCorrect/total




""" END utility functions for trees """
data1Dict = createCounter(project4.data1TrainingExamples,project4.data1TrainingLabels)
data2Dict = createCounter(project4.data2TrainingExamples,project4.data2TrainingLabels)

infoRoot = Node(data2Dict)
giniRoot = Node(data2Dict)
info1Root = Node(data1Dict)
gini1Root = Node(data1Dict)

createTreeInfo(infoRoot)
createTreeGini(giniRoot)
createTreeInfo(info1Root)
createTreeGini(gini1Root)
print "Infogain v GiniIndex -- Data Set 2 -- ",compareTree(infoRoot,giniRoot)
info2Class = project4.evaluateBinaryLearner(project4.data2TestExamples,project4.data2TestLabels,giniRoot)
print info2Class
#print "Percentage Correct - ",calculatePercentage(info2Class,project4.data2TestLabels)
"""
print "Infogain v GiniIndex -- Data Set 2 -- ",compareTree(infoRoot,giniRoot)


print "Classifying Infogain implementation -- Data Set 1 --"
info1Classifications = classifyList(project4.data1TestExamples,info1Root)
print info1Classifications
print "Classifying Infogain implementation -- Data Set 2 --"
info2Classifications = classifyList(project4.data2TestExamples,infoRoot)
print info2Classifications
print "Classifying Gini Index implementation -- Data Set 1 --"
gini1Classifications = classifyList(project4.data1TestExamples,gini1Root)
print gini1Classifications
"""


