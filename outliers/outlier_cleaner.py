#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    ### your code goes here

    error = (predictions - net_worths) ** 2  # create list of error
    cleaned_data = zip(ages, net_worths, error)  # Merge tuple
    cleaned_data = sorted(cleaned_data, key=lambda tup: tup[2])  # sort by tuple index 2 i.e. error
    limit = len(cleaned_data) * 0.9  # 90% of length
    cleaned_data = cleaned_data[:int(limit - 1)]  # Remove last 10% or retain first 90%

    # print("limit ", limit - 1)
    # print("length ", len(cleaned_data))
    # print("cleaned_data ", cleaned_data)

    return cleaned_data
