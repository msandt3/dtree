This particular program creates a binary decision tree for a specified training data set, and runs the decision tree algorithm on a testing data set. It also provides accuracy statistics for both the training and testing data sets.

To run the program simply use the following syntax
python project4.py <test> <train> <method>

<test> corresponds to the data set to perform testing on. The available selections are 
[test1,test2]

<train> corresponds to the data set to create your tree from. The available selections are 
[train1,train2]

<method> corresponds to the method by which we select the most important attribute in the decision tree algorithm. Selections are 
[infogain,gini]

You can also use -h or --help at runtime for a list of applicable arguments

**** COMMANDS *****
python project4.py test1 train1 infogain
python project4.py test1 train1 gini
python project4.py test2 train2 infogain
python project4.py test2 train2 gini
