"""
A00304351
Program to show data related to tech layoffs in the USA during 2022
"""
import read_file, menus

# Read data from csv file
company_size_list, total_funding_list, percentage_impacted_list = read_file.read()

# Open interactive user menu
menus.home_menu(company_size_list, total_funding_list, percentage_impacted_list)