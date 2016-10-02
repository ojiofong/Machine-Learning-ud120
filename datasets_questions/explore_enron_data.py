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

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))


total = len(enron_data)
print("enron data total:", total)
# print(enron_data)
# print(enron_data.keys())
# print(enron_data.values())

countPOI = 0;
countSalary = 0;
countEmail = 0;
countTotalPaymentNaN = 0;

for key,value in enron_data.items():
    # print(key, 'corresponds to', value)
    if enron_data[key]["poi"]:
            countPOI += 1

    if enron_data[key]["salary"] != 'NaN':
        countSalary += 1

    if enron_data[key]["email_address"] != 'NaN':
        countEmail += 1

    if enron_data[key]["poi"] and enron_data[key]["total_payments"] == 'NaN':
        countTotalPaymentNaN += 1

print("Total POI count:", countPOI)
print("Total Quantified Salary count:", countSalary)
print("Total Known Email:", countEmail)
print("Total Payments NaN:", countTotalPaymentNaN/countPOI * 100, "%")

print("\nJames Prentice's total stocks:", enron_data["PRENTICE JAMES"]['total_stock_value'])
print("email from Wesley Colwell to POI:", enron_data["COLWELL WESLEY"]['from_this_person_to_poi'])
print("Jeffrey K Skilling's stock options:", enron_data["SKILLING JEFFREY K"]['exercised_stock_options'])

