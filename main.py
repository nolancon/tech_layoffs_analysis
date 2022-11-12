# Program to show data related to tech layoffs in the USA during 2022

import display, analyse, read_file

company_size_list, total_funding_list, percentage_impacted_list = read_file.read()
display.display_total_funding_data(total_funding_list)
display.display_percentage_impacted_data(percentage_impacted_list)
display.display_correlation(total_funding_list, percentage_impacted_list)
display.display_subcategory_analysis(analyse.analyse_subcategory(company_size_list, percentage_impacted_list))
