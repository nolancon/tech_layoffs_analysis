"""
Functions to calculate statistics
"""

import math

def calc_mean(numbers):
    """
    Calculate the mean of the numbers in the list.
    
    Parameters
    ----------
    numbers : list
        A list of numbers.

    Returns
    -------
    float
        The mean of the list of numbers.
    """
    return float(sum(numbers)/len(numbers))

def calc_median(numbers):
    """
    Calculate the median of the numbers in the list.
    
    Parameters
    ----------
    numbers : list
        A list of numbers.

    Returns
    -------
    float
        The median of the list of numbers.
    """
    sorted_numbers = sorted(numbers)
    mid_index = int(len(sorted_numbers)/2)
    if len(sorted_numbers) % 2 == 1: # odd
        median = sorted_numbers[mid_index]
    else:
        median = (sorted_numbers[mid_index-1] + sorted_numbers[mid_index])/2  
    return float(median)

def calc_mode(numbers):
    """
    Calculate the mode of the numbers in the list.
    
    Parameters
    ----------
    numbers : list
        A list of numbers.

    Returns
    -------
    float
        The mode of the list of numbers.
    """
    uniques = sorted(set(numbers))
    frequencies = [ numbers.count(value) for value in uniques ]
    max_freq = max(frequencies)
    max_freq_index = frequencies.index(max_freq)
    return float(uniques[max_freq_index])

    
def calc_range(numbers):
    """
    Calculate the range of the numbers in the list.
    
    Parameters
    ----------
    numbers : list
        A list of numbers.

    Returns
    -------
    float
        The range of the list of numbers.
    """
    return float(max(numbers) - min(numbers))

     

def calc_iqr(numbers):
    """
    Calculate the inter-quartile range of the numbers in the list.
    
    Parameters
    ----------
    numbers : list
        A list of numbers.

    Returns
    -------
    float
        The inter-quartile range of the list of numbers.
    """
    sorted_numbers = sorted(numbers)
    mid_index = int(len(sorted_numbers)/2)
    if len(sorted_numbers) % 2 == 1: #odd
        lower_half = sorted_numbers[:mid_index]
        upper_half = sorted_numbers[mid_index+1:]
    else:
        lower_half = sorted_numbers[:mid_index]
        upper_half = sorted_numbers[mid_index:]
    
    return float((calc_median(upper_half) - calc_median(lower_half)))
    
def calc_std_dev(numbers):
    """
    Calculate the standard deviation of the numbers in the list.
    
    Parameters
    ----------
    numbers : list
        A list of numbers.

    Returns
    -------
    float
        The standard deviation of the list of numbers.
    """
    return float(math.sqrt(sum([ (x - calc_mean(numbers)) ** 2 for x in numbers ])/(len(numbers)-1)))

def calc_median_skewness(numbers):
    """
    Calculate the median skewness of the numbers in the list.
    
    Parameters
    ----------
    numbers : list
        A list of numbers.

    Returns
    -------
    float
        The median skewness of the list of numbers.
    """
    return float((3*(calc_mean(numbers)-calc_median(numbers)))/calc_std_dev(numbers))

def calc_mode_skewness(numbers):
    """
    Calculate the mode skewness of the numbers in the list.
    
    Parameters
    ----------
    numbers : list
        A list of numbers.

    Returns
    -------
    float
        The mode skewness of the list of numbers.
    """
    return float((calc_mean(numbers)-calc_mode(numbers))/calc_std_dev(numbers))

def calc_correlation(x_values, y_values):
    """
    Calculate the correlation between x_values and y_values.

    Parameters
    ----------
    x_values : list
        A list of numbers..
    y_values : list
        A list of numbers..

    Returns
    -------
    float
        The correlation between x_values and y_values.

    """
    x_mean = calc_mean(x_values)
    y_mean = calc_mean(y_values)
    x_deviations = [x - x_mean for x in x_values]
    y_deviations = [y - y_mean for y in y_values]
    xy_deviations = [ x*y for (x,y) in zip(x_deviations,y_deviations)] 
    x_squared_deviations = [ (x - x_mean) ** 2 for x in x_values ]
    y_squared_deviations = [ (y - y_mean) ** 2 for y in y_values ]      
    return float(sum(xy_deviations)/math.sqrt(sum(x_squared_deviations)*sum(y_squared_deviations)))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    