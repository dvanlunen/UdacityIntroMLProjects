#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building a POI identifier

    Start by loading/formatting the data...
"""

import pickle
import sys
from sklearn import tree
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.cross_validation import train_test_split
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


data_dict = pickle.load(open("../final_project/final_project_dataset.pkl",
                        "r"))

# features
features_list = ["poi", "salary"]
data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)


# make test train split and test classifier

features_train, features_test, labels_train, labels_test = train_test_split(
    features, labels, test_size=.3, random_state=42)


clf = tree.DecisionTreeClassifier()
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
print accuracy_score(pred, labels_test)
print precision_score(pred, labels_test)
print recall_score(pred, labels_test)

# check specific accuracy
print pred
print len(pred)
print labels_test
for i in range(29):
    print i, "pred:", pred[i], "true:", labels_test[i]
