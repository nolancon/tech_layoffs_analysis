# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 11:42:04 2022

@author: cmsno
"""

import analyse, sanitise, matplotlib.pyplot as plt

def percentage_impacted_hist(percentage_impacted_list):
    fig, ax = plt.subplots()
    ax.set_title("Employees Impacted per Layoff Announcement")
    ax.set_xlabel("Company Employees (%)")
    ax.set_ylabel("Number of Layoff Announcements")
    ax.hist(percentage_impacted_list)
    plt.show()

def percentage_impacted_box_plot(percentage_impacted_list):
    fig, ax = plt.subplots()
    ax.set_title("Tech Layoffs US 2022 (Excludinig Outliers)")
    ax.set_ylabel("Employees Impacted per Layoff Announcement (%)")
    ax.boxplot(percentage_impacted_list, showfliers=False)
    plt.show()
    
def impacted_per_funding_scatter_plot(total_funding_list, percentage_impacted_list):
    fig, ax = plt.subplots()
    ax.set_title("Tech Layoffs US 2022")
    ax.set_xlabel("Total Funding (millions $)")
    ax.set_ylabel("Employees Impacted per Layoff Announcement (%)")
    ax.scatter(sanitise.total_funding_in_millions(total_funding_list),percentage_impacted_list)
    plt.show()
    
def total_funding_hist(total_funding_list):
    fig, ax = plt.subplots()
    ax.set_title("Total Funding Received")
    ax.set_xlabel("Total Funding (millions $)")
    ax.set_ylabel("Number of Layoff Announcements")
    ax.hist(sanitise.total_funding_in_millions(total_funding_list))
    plt.show()

def total_funding_box_plot(total_funding_list):
    fig, ax = plt.subplots()
    ax.set_title("Tech Layoffs US 2022 (Excluding Outliers)")
    ax.set_ylabel("Total Funding of Company Announcing Layoffs (millions $)")
    ax.boxplot(sanitise.total_funding_in_millions(total_funding_list), showfliers=False)
    plt.show()

def percentage_impacted_pie_chart(company_size_list, percentage_impacted_list):
    layoff_announcements_per_company_size = analyse.layoff_announcements_per_company_size(company_size_list, percentage_impacted_list)
    fig, ax = plt.subplots()
    ax.set_title("US Tech Layoff Announcements per Company Size in 2022")
    ax.pie(layoff_announcements_per_company_size.values(), labels=layoff_announcements_per_company_size.keys(), autopct="%.1f%%")
    plt.show()