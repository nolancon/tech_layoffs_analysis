"""
 Helper functions to get numeric data, estimating when necessary 
"""

import stats

def get_percentage_impacted(num_layoffs, percentage_impacted, company_size):
    """
    Get the percentage of employees at the company impacted by the
    layoff announcement. Estimiate based on number of layoffs and 
    company size if percentage impacted has not been specified.
    Parameters
    ----------
    num_layoffs : string
        Number of layoffs announced.
    percentage_impacted : string
        Percentage of employees impacted.
    company_size : string
        Size of company announcing layoffs.

    Returns
    -------
    float
        Percentage of employees impacted.
    """
    try:
        return float(percentage_impacted.strip("%"))
    except:
        return float(estimate_percentage_impacted(num_layoffs, company_size))
    
    
def get_num_layoffs(num_layoffs, percentage_impacted, company_size):
    """
    Get the number of layoffs for the company. Estimate based
    on percentage impacted and company size if number of layoffs
    has not been specified.

    Parameters
    ----------
    num_layoffs : string
        Number of layoffs announced.
    percentage_impacted : string
        Percentage of employees impacted.
    company_size : string
        Size of company announcing layoffs.

    Returns
    -------
    float
        Number of employees layed off.
    """
    try:
        return float(num_layoffs)
    except:
        # cloud not convert to int, must be unclear. 
        # attempt estimate.
        return float(estimate_num_layoffs(percentage_impacted, company_size))


def estimate_percentage_impacted(num_layoffs, company_size):
    """
    Estimate the percentage of employees impacted based on
    number of layoffs and estimated company size.

    Parameters
    ----------
    num_layoffs : string
        Number of layoffs announced.
    company_size : TYPE
       Size of company announcing layoffs.

    Returns
    -------
    float
        Estimated percentage of employees impacted.

    """
    try:
        # estimate the number of employees impacted by
        # estimated company size and the number of layoffs.
        return float((num_layoffs)/int(estimate_num_employees(company_size)))
    except:
        return 0

def estimate_num_layoffs(percentage_impacted, company_size):
    """
    Estimate the number of employees layed off based on
    number on the percentage impacted and estimated company size.

    Parameters
    ----------
    percentage_impacted : TYPE
        Percentage of employees impacted.
    company_size : string
        Size of company announcing layoffs.

    Returns
    -------
    float
        Estimated number of emplyees layed off.

    """
    try:
        # estimate the number of layoffs by the estimated
        # company size and the % of workforce impacted.
        return float(estimate_num_employees(company_size) * (float(percentage_impacted.strip("%"))/100))
    except:
        return 0
    
def estimate_num_employees(company_size):
    """
    Estimate number of employees based on company size.
    An estimate is the mean of min and max employees as
    described by company size (eg 101-250).
    Max company size (10000+) estimate defaults to 10000.

    Parameters
    ----------
    company_size : string
        Size of company announcing layoffs..

    Returns
    -------
    float
        Estimated company size.

    """
    if "-" in company_size:
        # if the company size contains "-" e.g 51-100
        # get the mean of the min-max employees.
        min_employees, max_employees = company_size.split("-")
        return float(stats.calc_mean([int(min_employees), int(max_employees)]))
 
    elif "+" in company_size:
        # if the company size contains "+" eg 10000+
        # return that number as a conservative estimate
        return float(company_size[:-1])
    else:
        return 0
        
def get_total_funding(total_funding):
    """
    Get the company's total funding amount in dollars.

    Parameters
    ----------
    total_funding : string
        Total funding received by a company in millions of dollars.

    Returns
    -------
    float
        Total funding received by a company in dollars.

    """
    try:
        return float(int(total_funding)*1000000)
    except:
        return 0