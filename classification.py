from Node import *

def classifyList(examples, root):
	retlist = []
	for example in examples:
		retval = classifyExample(example,root)
		#retlist.append((example,retval))
		retlist.append(retval)
	return retlist

def classifyExample(example, root):
	if(root.examplesEmpty()):
		return root.getParent().getPluralityValue()
	elif(root.isYes()):
		return 1
	elif(root.isNo()):
		return 0
	elif(root.attributesEmpty()):
		return root.getPluralityValue()
	#otherwise remove the attribute split by
	else:
		attrval = example[root.getAttrNum()]
		example.pop(root.attrnum)

		if attrval == 1:
			return classifyExample(example,root.getChildren()[0])
		else:
			return classifyExample(example,root.getChildren()[1])