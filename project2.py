#!/usr/bin/python
import numpy as np
import math
import copy
import sys, getopt

def read_data(file_name):
    file = open(file_name, 'r')
    lines = file.readlines()
    k = len(lines[0].split())
    n = len(lines)
    data = np.zeros((n,k))
    for i in range(n):
        line_words = lines[i].split()
        for j in range(k):
            data[i,j] = eval(line_words[j])
    labels = data[:,0]
    features = data[:,1:]
    features = (features - np.mean(features,axis = 0))/np.var(features, axis=0) #normalize features
    return labels, features

def leave_one_accuracy(labels, features):
    n = len(labels)
    correct_count = 0
    for i in range(n):
        distance_array = np.sum(np.power((features - features[i]),2), axis = 1)
        distance_array[i] = 100000  #max value
        nearest_neighbor = int(np.argmin(distance_array))
        correct_count += (labels[i] == labels[nearest_neighbor])
    return correct_count / n

def forward_selection(file_name):
    labels, features = read_data(file_name)
    m = np.shape(features)[1]
    print("The data has {} features in total.".format(m))
    indeces = [i for i in range(m)]
    selection = []
    best_features = []
    best_accuracy = 0
    for i in range(m):
        print("in {}th round".format(i+1))
        max_accuracy = 0
        max_index = -1
        for f in indeces:
            current_select = copy.copy(selection)
            current_select.append(f)
            accuracy = leave_one_accuracy(labels, features[:,current_select])
            print("select feature {}, with accuracy {}".format(f+1, accuracy))
            if (accuracy > max_accuracy):
                max_accuracy = accuracy
                max_index = f
        selection.append(max_index)
        indeces.remove(max_index)
        print("feature set {} was best, with accuracy {}".format([i+1 for i in selection], max_accuracy))
        if max_accuracy > best_accuracy :
            best_accuracy = max_accuracy
            best_features = copy.copy(selection)
    print("Finished search! The best feature set is {}. with accuracy {}.".format([i+1 for i in best_features], best_accuracy))
                
def backward_elimination(file_name):
    labels, features = read_data(file_name)
    m = np.shape(features)[1]
    print("The data has {} featuers in total.".format(m))
    selection = [i for i in range(m)]
    best_features = []
    best_accuracy = 0
    for i in range(m-1):
        print("in {}th round".format(i+1))
        max_accuracy = 0
        max_index = -1
        for f in selection:
            current_indeces = copy.copy(selection)
            current_indeces.remove(f)
            accuracy = leave_one_accuracy(labels, features[:,current_indeces])
            print("remove feature {}, with accuracy {}".format(f+1,accuracy))
            if (accuracy > max_accuracy):
                max_accuracy = accuracy
                max_index = f
        selection.remove(max_index)
        print("feature set {} was best, with accuracy {}".format([i+1 for i in selection], max_accuracy))
        if max_accuracy > best_accuracy :
            best_accuracy = max_accuracy
            best_features = copy.copy(selection)
    print("Finished search! The best feature set is {}. with accuracy {}.".format([i+1 for i in best_features], best_accuracy))


def main():
    print(sys.argv)
    if len(sys.argv) != 3:
        print("usage: python project2.py <filename> <algorithm: 0 is forward selection, 1 is backward elemination>")
        sys.exit()
    file_name = sys.argv[1]
    algorithm = eval(sys.argv[2])
    if algorithm==0:
        forward_selection(file_name)
    else:
        backward_elimination(file_name)
    

if __name__ == "__main__":
   main()