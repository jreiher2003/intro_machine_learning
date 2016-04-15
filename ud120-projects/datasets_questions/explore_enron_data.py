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
pprint(len(enron_data["SKILLING JEFFREY K"].keys()))
pprint(enron_data["SKILLING JEFFREY K"])

peeps = enron_data.keys()

poi = []		
for k, v in enron_data.iteritems():
	if v['poi'] == 1:
		poi.append(k)
		# print k
# print poi
print len(poi)

pprint(enron_data['PRENTICE JAMES'])
pprint(enron_data["COLWELL WESLEY"])
		
		# print len(k)




