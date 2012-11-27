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
def createTree(node):
	print "Node - ",node," \n",node.toString()
	#children = node.createChildren()
	children = node.createChildrenGini()

	for child in children:
		print "Child - ",child," \n",child.toString()
		#if examples empty, return parent plurality value
		if(child.examplesEmpty()):
			print "Examples empty"
			#return
		#if labels empty return child plurality value
		elif(child.attributesEmpty()):
			print "Attributes empty"
			#return
		#if we can determine yes or no
		elif(child.isYes() or child.isNo()):
			print "Yes or no decision"
			#return
		else:
			createTree(child)

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
		retlist.append((example,retval))
	return retlist

def classifyExample(example, root):
	print root.toString()
	print root.attrnum
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


""" END utility functions for trees """

originalDict = createCounter(project4.data1TrainingExamples,project4.data1TrainingLabels)
#debugDict = createCounter(tryEx1,tryLa1)
#root = Node(debugDict)

#print "Original Values\n",toString(originalDict)
root = Node(originalDict)
createTree(root)
traverseTree(root)

#vals = classifyList(project4.data2TestExamples,root)
#toString(vals)
"""
print "Comparison test, roots data - \n",root.toString()
for child in root.getChildren():
	print "Child - ",child," data\n"
	print child.toString()
"""
#root = Node(project4.data1TrainingExamples,project4.data1TrainingLabels)

#createTree(root)
#traverseTree(root)
#children = root.createChildren()
#print root.sDebug()
#print root.getPluralityValue()
#children = root.getChildren()
#children[0].sDebug()



