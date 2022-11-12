# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 19:47:11 2022

@author: cmsno
"""

import stats

def analyse_subcategory(company_size_list, percentage_impacted_list):
    percentage_impacted_by_company_size = {}
    percentage_impacted_by_company_size["Number of Company Sizes"] = len(set(company_size_list))
    percentage_impacted_by_company_size["Company Size with Most Layoff Announcements"] = company_size_most_occurrences(company_size_list)
    percentage_impacted_by_company_size["Company Size with Least Layoff Announcements"] = company_size_least_occurrences(company_size_list)    
    percentage_impacted_by_company_size["Company Size with Highest Average Percentage of Impacted Employees"] = highest_avg(avg_impacted_in_subs(split_pct_impacted_into_subs(company_size_list, percentage_impacted_list)))
    percentage_impacted_by_company_size["Company Size with Lowest Average Percentage of Impacted Employees"] = lowest_avg(avg_impacted_in_subs(split_pct_impacted_into_subs(company_size_list, percentage_impacted_list)))
    return percentage_impacted_by_company_size

def company_size_most_occurrences(company_size_list):
    uniques = set(company_size_list)
    frequencies = [ company_size_list.count(value) for value in uniques ]
    max_freq = max(frequencies)
    max_freq_index = frequencies.index(max_freq)
    return format_count_outputs(company_size_list[max_freq_index], max_freq)
            
def company_size_least_occurrences(company_size_list):
    uniques = set(company_size_list)
    frequencies = [ company_size_list.count(value) for value in uniques ]
    min_freq = min(frequencies)
    min_freq_index = frequencies.index(min_freq)
    return format_count_outputs(company_size_list[min_freq_index], min_freq)
    
def split_pct_impacted_into_subs(company_size_list, percentage_impacted_list):     
    size_to_impacted = {}
    unique_company_sizes = set(company_size_list) 
    for company_size in unique_company_sizes:
        percentages = []
        i = 0
        for percentage_impacted in percentage_impacted_list:
            if company_size_list[i] == company_size:
                percentages.append(percentage_impacted)
            size_to_impacted[company_size] = percentages
            i = i + 1
            
    return size_to_impacted

def avg_impacted_in_subs(size_to_impacted):
    size_to_avg = {}
    for company_size in size_to_impacted:
        size_to_avg[company_size] = round(stats.calc_mean(size_to_impacted[company_size]),2)
    return size_to_avg
    
def highest_avg(size_to_avg):
    largest_avg = 0
    company_size_with_largest_avg = ""
    for company_size in size_to_avg:
        if size_to_avg[company_size] > largest_avg:
            largest_avg = size_to_avg[company_size]
            company_size_with_largest_avg = company_size
    
    return format_pct_outputs(company_size_with_largest_avg, largest_avg)
       
def lowest_avg(size_to_avg):
    lowest_avg = 100
    company_size_with_lowest_avg = ""
    for company_size in size_to_avg:
        if size_to_avg[company_size] < lowest_avg:
            lowest_avg = size_to_avg[company_size]
            company_size_with_lowest_avg = company_size
    
    return format_pct_outputs(company_size_with_lowest_avg, lowest_avg)
    
def format_count_outputs(sub_cat, value):
    return str(sub_cat + " (" + str(value) + ")")

def format_pct_outputs(sub_cat, value):
    return str(sub_cat + " (" + str(value) + "%)")               