#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import cPickle
from pprint import pprint

enron_data = cPickle.load(open("../final_project/final_project_dataset.pkl", "r"))

pprint(len(enron_data))
# pprint(len(enron_data["SKILLING JEFFREY K"].keys()))

# peeps = enron_data.keys()
# print peeps
poi = []        
for k, v in enron_data.iteritems():
    if v['poi'] == 1:
        poi.append(k)
        # print k
# print poi
print len(poi)

pprint(enron_data['LAY KENNETH L'])
# pprint(enron_data['FASTOW ANDREW S'])
# pprint(enron_data["SKILLING JEFFREY K"])
		
		# print len(k)


qs = []
for k, v in enron_data.iteritems():
    if v['salary'] != 'NaN':
        qs.append(k)

print len(qs)

email = []
for k, v in enron_data.iteritems():
    if v['email_address'] != 'NaN':
        email.append(k)

print len(email)

tp = []
for k, v in enron_data.iteritems():
    if v['total_payments'] == 'NaN':
        tp.append(k)
        print v["total_payments"]
print len(tp)

tsv = []
for k, v in enron_data.iteritems():
    if v['total_stock_value'] == 'NaN':
        tsv.append(k)
        
print len(tsv)