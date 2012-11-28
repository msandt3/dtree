import util
import math
import copy

""" Begin GINI Index methods """
""" Note this implementation is 
	restricted to binary classification """

def giniIndexSet(counter):
	""" Determines the gini index for a set of binary
	example/label pairs """
	#print "Computing gini index for set ",counter
	fitems = 0.0
	titems = 0.0
	total = 0.0
	if not counter:
		return 1
	for item in counter:
		if item[1] == 0:
			fitems += 1
		elif item[1] == 1:
			titems += 1
		total += 1
	freq0 = math.pow((fitems/total),2)
	freq1 = math.pow((titems/total),2)
	return 1 - (freq0 + freq1)

def detBestAttr(counter):
	""" This method determines the attribute with the lowest
		gini score. It determines the gini score for the subsets
		which said yes and no for a particular attribute """
	n = float(len(counter))
	minGini = float("inf")
	minAttr = 0
	for attr in range(0,len(counter[0][0])):
		yes,no = splitByAttr(counter,attr)
		n1 = float(len(yes))
		n2 = float(len(no))
		giniScore = ((n1/n)*giniIndexSet(yes) + (n2/n)*giniIndexSet(no))
		if  giniScore < minGini:
			minGini = giniScore
			minAttr = attr
	return minAttr

def splitByAttr(counter, attr):
	""" This method splits examples by a particular attribute
		removing the attribute split by and splitting the labels
		based on their associated attribute
	"""
	yes = []
	no = []
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
