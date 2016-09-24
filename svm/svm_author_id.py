#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

from sklearn import svm
# clf = svm.SVC(kernel='linear')
clf = svm.SVC(kernel='rbf', C=10000)

# start timing
t0 = time()

# Slice data down to 1%
# features_train = features_train[:int(len(features_train)/100)]
# labels_train = labels_train[:int(len(labels_train)/100)]

clf.fit(features_train, labels_train)

print("training/fitting time:", round(time()-t0, 3), "s")

# start timing
t0 = time()
# prediction
pred = clf.predict(features_test)
print("Prediction: ", pred[10])
print("Prediction: ", pred[26])
print("Prediction: ", pred[50])

print("prediction time:", round(time()-t0, 3), "s")


print("Label Chris (1): ", list(pred).count(1))

# accuracy
# accuracy = clf.score(features_train, labels_train)
# print(accuracy)

# Preferred accuracy API.. Uses pred
from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)
print("Accuracy_score: ", acc)


# SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
#     decision_function_shape=None, degree=3, gamma='auto', kernel='rbf',
#     max_iter=-1, probability=False, random_state=None, shrinking=True,
#     tol=0.001, verbose=False)

#########################################################


