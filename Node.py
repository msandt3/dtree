import infogain
import util
import random
import gini
""" This is a node data structure for a binary implementation of
	a decision tree """
class Node:
	def __init__(self, counter, parent=None, attrnum=None):
		self.parent = parent
		self.counter = counter
		self.attrnum = attrnum
		#Children decided by yes will be first entry in list, no second
		self.children = []
		#not sure about including a yes & no child

		self.noChild = None
		self.yesChild = None 
		
		if(attrnum != None):
			self.name = "Node split at attribute",attrnum

	def getCounter(self):
		return self.counter
	def setCounter(self,counter):
		self.counter = counter
	""" Attribute num is the attribute we chose to split by """
	def setAttrNum(self, attrNum):
		self.attrnum = attrNum
	def getAttrNum(self):
		return self.attrnum

	def setChildren(self, children):
		self.children = children
	def getChildren(self):
		return self.children
	def setParent(self, parent):
		self.parent = parent
	def getParent(self):
		return self.parent
	""" END GETTERS AND SETTERS """

	def addChildNode(self, newNode):
		self.children.append(newNode)
	def removeChildNode(self, child):
		if child in children:
			remove(child)

	""" FUNCTIONS FOR DETERMINING YES/NO DECISIONS """
	def isYes(self):
		count = util.Counter()
		for item in self.counter:
			count[item[1]] += 1
		if(count[0] == 0):
			return True
		else:
			return False

	def isNo(self):
		count = util.Counter()
		for item in self.counter:
			count[item[1]] += 1
		if(count[1] == 0):
			return True
		else:
			return False

	def createChildrenInfo(self):
		self.attrnum = infogain.detBestAttr(self.counter)
		#print "Splitting by attribute - ",self.attrnum
		yesno = infogain.splitByAttr(self.counter, self.attrnum)

		children = []
		for item in yesno:
			temp = Node(item,self)
			self.addChildNode(temp)
		return self.children
	def createChildrenGini(self):
		self.attrnum = gini.detBestAttr(self.counter)
		#print "Attribute selected - ",self.attrnum
		yesno = gini.splitByAttr(self.counter, self.attrnum)

		children = []
		for item in yesno:
			temp = Node(item,self)
			self.addChildNode(temp)
		return self.children

	def examplesEmpty(self):
		return not(len(self.counter))
	def attributesEmpty(self):
		for item in self.counter:
			if len(item[0]) > 0:
				return False
		return True
	def toString(self):
		if self.parent == None:
			print "Root node",self
			print "split by - ",self.attrnum
			print ""
		else:
			print "Node at ",self
			print "Child of ",self.parent
			if(self.isYes()):
				print "Yes decision"
			elif self.isNo():
				print "No decision"
			else:
				print "split by - ",self.attrnum
			print ""
	def getPluralityValue(self):
		nT = 0
		nF = 0
		for label in self.labels:
			if label == 1:
				nT += 1
			else:
				nF += 1
		if nT > nF:
			return 1
		elif nF > nT:
			return 0
		#not sure about this one
		else:
			return random.randint(0,1)

	""" DEBUGGING METHODS """
	def sDebug(self):
		if(self.parent == None):
			print "Root Node \n"
			print "Counter - ",self.counter,"\n"
			print "Attrbute split - ",self.attrnum,"\n"
			print "Children - ",self.children
		else:
			print "Parent Node",self.parent,"\n"
			print "Examples - ",self.examples,"\n"
			print "Labels - ",self.labels,"\n"
		
		for c in range(len(self.children)):
			if self.children != None:
				print "Child ",c,"\n"
				self.children[c].sDebug()



