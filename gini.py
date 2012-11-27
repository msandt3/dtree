import util
import math
import copy

""" Begin GINI Index methods """
""" Note this implementation is 
	restricted to binary classification """


def giniIndexSet(counter):
	""" Determines the gini index for a set of binary
	example/label pairs """
	fitems = 0
	titems = 0
	total = 0

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
	n = len(counter)
	minGini = float("inf")
	minAttr = 0
	for item in counter:
		for attr in range(0,len[item]):
			yes,no = splitByAttr(counter,attr)
			n1 = len(yes)
			n2 = len(no)

			if ((n1/n)*giniIndexSet(yes) + (n2/n)*giniIndexSet(no)) < minGini:
				minGini = ((n1/n)*giniIndexSet(yes) + (n2/n)*giniIndexSet(no))
				minAttr = attr


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
