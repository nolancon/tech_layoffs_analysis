# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 16:31:54 2022

@author: cmsno
"""
import stats

def get_percentage_impacted(num_layoffs, percentage_impacted, company_size):
    try:
        return float(percentage_impacted.strip("%"))
    except:
        return estimate_percentage_impacted(num_layoffs, company_size)
    
    
def get_num_layoffs(num_layoffs, percentage_impacted, company_size):
    try:
        return int(num_layoffs)
    except:
        # cloud not convert to int, must be unclear. 
        # attempt estimate.
        return estimate_num_layoffs(percentage_impacted, company_size)


def estimate_percentage_impacted(num_layoffs, company_size):
    try:
        # estimate the number of employees impacted by
        # estimated company size and the number of layoffs.
        return int(num_layoffs)/int(estimate_num_employees(company_size))
    except:
        return 0

def estimate_num_layoffs(percentage_impacted, company_size):
    try:
        # estimate the number of layoffs by the estimated
        # company size and the % of workforce impacted.
        return int(estimate_num_employees(company_size) * (float(percentage_impacted.strip("%"))/100))
    except:
        return 0
    
def estimate_num_employees(company_size):
    if "-" in company_size:
        # if the company size contains "-" e.g 51-100
        # get the mean of the min-max employees.
        min_employees, max_employees = company_size.split("-")
        return stats.calc_mean([int(min_employees), int(max_employees)])
 
    elif "+" in company_size:
        # if the company size contains "+" eg 10000+
        # return that number as a conservative estimate
        return company_size[:-1]
    else:
        return 0
        
def get_total_funding(total_funding):
    try:
        return int(total_funding)*1000000
    except:
        return 0
    
def total_funding_in_millions(total_funding_list):
    total_funding_list_in_millions = []
    for total_funding in total_funding_list:
        total_funding_list_in_millions.append(total_funding/1000000)
    return total_funding_list_in_millions