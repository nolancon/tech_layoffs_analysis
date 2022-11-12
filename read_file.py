# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 20:47:37 2022

@author: cmsno
"""
import sys, sanitise

file_path = "tech_layoffs_us_2022.csv"

def read():
    total_funding_list = []
    percentage_impacted_list = []
    company_size_list = []
       
    with open(file_path) as data_file:
        _ = data_file.readline()
        for line in data_file:
            _, num_layoffs, percentage_impacted, _, _, _, _, _, total_funding, company_size = line.split(",")
            # we need to sanitise the numeric data 
            total_funding = sanitise.get_total_funding(total_funding)
            percentage_impacted = sanitise.get_percentage_impacted(num_layoffs.strip(), percentage_impacted.strip(), company_size.strip())
            # ignore invalid numeric entries as the will skew the data.
            if total_funding == 0 or percentage_impacted == 0:
                continue
            percentage_impacted_list.append(percentage_impacted)    
            total_funding_list.append(total_funding)
            company_size_list.append(company_size.strip())
    
    # ensure all columns are the same length, otherwise data will be mixed up
    if False == (len(percentage_impacted_list)==len(total_funding_list)==len(company_size_list)):
        print("All columns are not equal in length, please revise the input data before proceeding.")
        sys.exit()
        
    return company_size_list, total_funding_list, percentage_impacted_list