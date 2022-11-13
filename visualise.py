"""
Functions to display visualisations such as charts, plots etcd
"""

import analyse, sanitise, matplotlib.pyplot as plt

def percentage_impacted_hist(percentage_impacted_list):
    """
    Display a histogram of percentage of employees impacted per 
    layoff announcement.

    Parameters
    ----------
    percentage_impacted_list : list
        List of percentages of employees impacted per layoff 
        announcement.

    Returns
    -------
    None.

    """
    fig, ax = plt.subplots()
    ax.set_title("Employees Impacted per Layoff Announcement")
    ax.set_xlabel("Company Employees (%)")
    ax.set_ylabel("Number of Layoff Announcements")
    ax.hist(percentage_impacted_list)
    plt.show()

def percentage_impacted_box_plot(percentage_impacted_list):
    """
    Display a box plot of percentage of employees impacted per 
    layoff announcement.

    Parameters
    ----------
    percentage_impacted_list : list
        List of percentages of employees impacted per layoff 
        announcement.

    Returns
    -------
    None.

    """
    fig, ax = plt.subplots()
    ax.set_title("Tech Layoffs US 2022 (Excludinig Outliers)")
    ax.set_ylabel("Employees Impacted per Layoff Announcement (%)")
    ax.boxplot(percentage_impacted_list, showfliers=False)
    plt.show()
    
def impacted_per_funding_scatter_plot(total_funding_list, percentage_impacted_list):
    """
    Display a scatter plot of percentages of employees impacted
    per layoff announcement versus total funding received by company
    announcing layoffs.

    Parameters
    ----------
    total_funding_list : list
        List of total fnudings received by companys announcing 
        layoffs.
    percentage_impacted_list : list
        List of percentages of employees impacted per layoff 
        announcement.

    Returns
    -------
    None.

    """
    fig, ax = plt.subplots()
    ax.set_title("Tech Layoffs US 2022")
    ax.set_xlabel("Total Funding (millions $)")
    ax.set_ylabel("Employees Impacted per Layoff Announcement (%)")
    ax.scatter(sanitise.total_funding_in_millions(total_funding_list),percentage_impacted_list)
    plt.show()
    
def total_funding_hist(total_funding_list):
    """
    Display a histogram of total funding received by company
    announcing layoffs.

    Parameters
    ----------
    total_funding_list : list
        List of total fnudings received by companys announcing 
        layoffs.

    Returns
    -------
    None.

    """
    fig, ax = plt.subplots()
    ax.set_title("Total Funding Received")
    ax.set_xlabel("Total Funding (millions $)")
    ax.set_ylabel("Number of Layoff Announcements")
    ax.hist(sanitise.total_funding_in_millions(total_funding_list))
    plt.show()

def total_funding_box_plot(total_funding_list):
    """
    Display a box-plot of total funding received by company
    announcing layoffs.

    Parameters
    ----------
    total_funding_list : list
        List of total fnudings received by companys announcing 
        layoffs.

    Returns
    -------
    None.

    """
    fig, ax = plt.subplots()
    ax.set_title("Tech Layoffs US 2022 (Excluding Outliers)")
    ax.set_ylabel("Total Funding of Company Announcing Layoffs (millions $)")
    ax.boxplot(sanitise.total_funding_in_millions(total_funding_list), showfliers=False)
    plt.show()

def announcements_per_size_pie_chart(company_size_list, percentage_impacted_list):
    """
    Display a pie-chart of layoff announcements per company size.

    Parameters
    ----------
    company_size_list : list
        List of sizes of companies announcing layoffs.
    percentage_impacted_list : list
        List of percentages of employees impacted per layoff 
        announcement.

    Returns
    -------
    None.

    """
    layoff_announcements_per_company_size = analyse.layoff_announcements_per_company_size(company_size_list, percentage_impacted_list)
    fig, ax = plt.subplots()
    ax.set_title("US Tech Layoff Announcements per Company Size in 2022")
    ax.pie(layoff_announcements_per_company_size.values(), labels=layoff_announcements_per_company_size.keys(), autopct="%.1f%%")
    plt.show()
    
def avg_percentage_impacted_per_size_bar_chart(company_size_list, percentage_impacted_list):
    """
    Display bar chart of company size versus average percentage
    of employees impacted.

    Parameters
    ----------
    company_size_list : list
        List of sizes of companies announcing layoffs.
    percentage_impacted_list : list
        List of percentages of employees impacted per layoff 
        announcement.

    Returns
    -------
    None.

    """
    avg_percentage_impacted_per_size = analyse.avg_impacted_in_subs(analyse.split_pct_impacted_into_subs(company_size_list, percentage_impacted_list))
    fig, ax = plt.subplots()
    ax.set_title("US Tech Layoff Announcements per Company Size in 2022")
    ax.set_xlabel("Average Percentage of Employees Impacted")
    ax.set_ylabel("Company Size")
    y_pos = [ i for i in range(len(avg_percentage_impacted_per_size))] 
    ax.set_yticks(y_pos)
    ax.set_yticklabels(avg_percentage_impacted_per_size.keys())  
    for index, value in enumerate(avg_percentage_impacted_per_size.values()):
        ax.text(value, index-0.25, str(value))        
    ax.barh(y_pos, avg_percentage_impacted_per_size.values(), align="center")
    plt.show()
    
def avg_percentage_impacted_per_size_box_plots(company_size_list, percentage_impacted_list):
    """
    Display multiple box-plots of company size versus average percentage
    of employees impacted.

    Parameters
    ----------
    company_size_list : list
        List of sizes of companies announcing layoffs.
    percentage_impacted_list : list
        List of percentages of employees impacted per layoff 
        announcement.


    Returns
    -------
    None.

    """
    avg_percentage_impacted_per_size = analyse.split_pct_impacted_into_subs(company_size_list, percentage_impacted_list)
    fig, ax = plt.subplots()
    ax.set_title("US Tech Layoff Announcements per Company Size in 2022")
    ax.set_xlabel("Average Percentage of Employees Impacted")
    ax.set_ylabel("Company Size")
    ax.boxplot(avg_percentage_impacted_per_size.values(), showfliers=False, vert=False, labels=avg_percentage_impacted_per_size.keys())
   
    plt.show()