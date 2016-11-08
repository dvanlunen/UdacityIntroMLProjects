#!/usr/bin/python

"""
    Code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl",
                              "r"))

print enron_data["PRENTICE JAMES"].keys()

stock_opts = []
for name in enron_data:
    if enron_data[name]['salary'] > 12000000 and
    not type(enron_data[name]['salary']) is str:
        print name
    stock_opts.append(enron_data[name]['salary'])
print max(stock_opts)
print min(stock_opts)
print sorted(stock_opts)
