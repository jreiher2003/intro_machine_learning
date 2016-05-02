#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    net_worth = net_worth_train
    ages = ages_train
    predictions = reg.predict(ages_train)
    cleaned_data = []

    ### your code goes here
    # subtract net_worths from predictions
    # return tuple age, net_worth, error
    import operator
    errors = map(operator.sub, net_worth, predictions)

    cleaned_data = zip(ages, net_worth, errors)
    from operator import itemgetter
    cleaned_data = sorted(cleaned_data, key=itemgetter(2))
    print cleaned_data
    

    
    return cleaned_data

