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
    for i in range(len(predictions)):
        tup2add = (ages[i][0], net_worths[i][0],
                   abs(net_worths[i][0] - predictions[i][0]))
        cleaned_data.append(tup2add)
    cleaned_data.sort(key=lambda tup: tup[2])
    cleaned_data = cleaned_data[:int(len(cleaned_data)*0.9) - 1]
    return cleaned_data
