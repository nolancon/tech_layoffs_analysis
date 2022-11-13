"""
Program to show data related to tech layoffs in the USA during 2022
"""
import display, analyse, read_file, visualise

# Read data from csv file
company_size_list, total_funding_list, percentage_impacted_list = read_file.read()

# Display data of numeric categories
display.display_total_funding_data(total_funding_list)
display.display_percentage_impacted_data(percentage_impacted_list)

# Display correlation between numeric categories
display.display_correlation(total_funding_list, percentage_impacted_list)

# Display subcategory analysis of percentage of employees impacted per company size
display.display_subcategory_analysis(analyse.analyse_subcategory(company_size_list, percentage_impacted_list))

# Visualise data of percentage of employees impacted
visualise.percentage_impacted_hist(percentage_impacted_list)
visualise.percentage_impacted_box_plot(percentage_impacted_list)

# Visualise data of company funding
visualise.total_funding_hist(total_funding_list)
visualise.total_funding_box_plot(total_funding_list)

# Visualise correlation of subcategories
visualise.impacted_per_funding_scatter_plot(total_funding_list, percentage_impacted_list)

# Pie-chart of layoff announcements per company size
visualise.announcements_per_size_pie_chart(company_size_list, percentage_impacted_list)

# Bar-chart of average % impacted per company size
visualise.avg_percentage_impacted_per_size_bar_chart(company_size_list, percentage_impacted_list)

# Box-plots of % impacted per company size
visualise.avg_percentage_impacted_per_size_box_plots(company_size_list, percentage_impacted_list)