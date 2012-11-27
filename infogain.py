import util
import math
import copy

""" Begin information gain methods """
#determines the best attribute 
def detBestAttr(counter):
	#dictionary of attributes storing their information gain
	attributes = util.Counter()
	for item in counter:
		for i in range(0,len(item[0])):
			attributes[i] = gain(counter,i)
	return attributes.argMax()
			
#determines the information gain for a particular attribute
def gain(counter, attr):
	#print "Calculating infogain for attr ",attr
	p = float(getPositiveForAttr(counter, attr))
	n = float(getNegativeForAttr(counter, attr))
	return entropyBoolRandom(p/(p+n)) - binary_remainder(counter, attr)
	

#determines the remainder for a binary classification of an attribute
def binary_remainder(counter, attr):
	remvals = util.Counter()
	total = 0.0
	for i in range(0,2):
		#print "Calculating remainder for attrval ",i
		pk = getPositiveForAttrVal(counter, attr, i)
		nk = getNegativeForAttrVal(counter, attr, i)
		p = getPositiveForAttr(counter, attr)
		n = getNegativeForAttr(counter, attr)
		#print "pk: ",pk," nk: ",nk," p: ",p," n: ",n
		try:
			total += ((pk+nk)/(p+n))*entropyBoolRandom(pk/(pk+nk))
		except ZeroDivisionError:
			total += 0
	return float(total)

#this method determines the number of negative entries for specific val of attribute
def getNegativeForAttrVal(counter,attr,attrval):
	i = 0
	for item in counter:
		if(item[1] == 0):
			if(item[0][attr] == attrval):
				i += 1
	return float(i)
#this method determines number of pos entries for specific val of attribute
def getPositiveForAttrVal(counter,attr,attrval):
	i = 0
	for item in counter:
		if item[1] == 1:
			if(item[0][attr] == attrval):
				i += 1
	return float(i)
#returns total positive for a particular attribute
def getPositiveForAttr(counter,attr):
	i = 0
	for item in counter:
		if item[1] == 1:
			i += 1
	return float(i)
#returns total negative for attribute
def getNegativeForAttr(counter, attr):
	i = 0
	for item in counter:
		if item[1] == 0:
			i += 1
	return float(i)

		
def entropyBoolRandom(q):
	if q == 1.0:
		return -1*(q*math.log(q,2))
	elif q == 0.0:
		return -1*(1*math.log(1,2))
	else:
		return -1*(q*math.log(q,2)+(1.0-q)*math.log((1.0-q),2))

def splitByAttr(counter, attr):
	""" This method splits examples by a particular attribute
		removing the attribute split by and splitting the labels
		based on their associated attribute
	"""
	yes = []
	no = []
	#ylabel = []
	#nlabel = []
	#print examples
	#print labels
	i = 0
	j = 0
	for item in counter:
		if item[0][attr] == 1:
			yes.append(copy.deepcopy(item))
			yes[i][0].pop(attr)
			i += 1
		else:
			no.append(copy.deepcopy(item))
			no[j][0].pop(attr)
			j += 1
	return (yes,no)
	
""" End Information Gain methods """