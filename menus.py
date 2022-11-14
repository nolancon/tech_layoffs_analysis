"""
A00304351
Functions to navigate interactive user menus.
"""
import sys, display, analyse, visualise

sub_menu_prompt = "Please select an option from the menu: (0 to return to home menu):\n"

def total_funding_menu(total_funding_list):
    """
    Display user menu for total funding analysis.

    Parameters
    ----------
    total_funding_list : list
        List of total fnudings received by companys announcing 
        layoffs.

    Returns
    -------
    None.

    """
    user_input = -1
    while user_input != 0:
        print("""
Menu:
1. Display Analysis of Total Funding Recieved per Company.
2. Display Histogram of Total Funding Recieved per Company.
3. Display Box-Plot of Total Funding Recieved per Company.
        """)
        user_input = input(sub_menu_prompt)
        try:
           user_input = int(user_input)
        except:
           print("Invalid entry")
           continue
        if user_input == 1:
            # display percentage impacted analysis
            display.display_total_funding_data(total_funding_list)
        elif user_input == 2:
            # Visualise data of company funding (hist)
            visualise.total_funding_hist(total_funding_list)
        elif user_input == 3:
            # Visualise data of company funding (box plot)
            visualise.total_funding_box_plot(total_funding_list)
        elif user_input == 0:
            break
        else:
            print("Invalid entry")
            continue
    return
            

def percentage_impacted_menu(percentage_impacted_list):
    """
    Display user menu for percentage of employees impacted 
    analysis

    Parameters
    ----------
    percentage_impacted_list : list
        List of percentages of employees impacted per layoff 
        announcement.

    Returns
    -------
    None.

    """
    user_input = -1
    while user_input != 0:
        print("""
Menu:
1. Display Analysis of Percentages of Employees Impacted.
2. Display Histogram of Percentages of Employees Impacted.
3. Display Box-Plot of Percentages of Employees Impacted.
        """)
        user_input = input(sub_menu_prompt)
        try:
           user_input = int(user_input)
        except:
           print("Invalid entry")
           continue
        if user_input == 1:
            # display percentage impacted analysis
            display.display_percentage_impacted_data(percentage_impacted_list)
        elif user_input == 2:
            # Visualise data of percentage of employees impacted (hist)
            visualise.percentage_impacted_hist(percentage_impacted_list)
        elif user_input == 3:
            # Visualise data of percentage of employees impacted (box plot)
            visualise.percentage_impacted_box_plot(percentage_impacted_list)
        elif user_input == 0:
            break
        else:
            print("Invalid entry")
            continue
    return


def correlation_menu(total_funding_list, percentage_impacted_list):
    """
    Display user menu for correlation betweem percentage of employees 
    impacted and total funding received.

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
    user_input = -1  
    while user_input != 0:
        print("""
Menu:
1. Display Correlation Between Total Funding Recieved per Company 
   and Percentages of Employees Impacted.
2. Display Scatter-Plot of Percentages of Employees Impacted
   Versus Total Funding Recieved per Company.
        """)
        user_input = input(sub_menu_prompt)
        try:
           user_input = int(user_input)
        except:
           print("Invalid entry")
           continue
        if user_input == 1:
            # display correlation of subcategories
            display.display_correlation(total_funding_list, percentage_impacted_list)
        elif user_input == 2:
            # Visualise correlation of subcategories
            visualise.impacted_per_funding_scatter_plot(total_funding_list, percentage_impacted_list)
        elif user_input == 0:
            break
        else:
            print("Invalid entry")
    return
 
def analysis_by_company_size_menu(total_funding_list, percentage_impacted_list, company_size_list):
    """
    Display user menu for analysis of percentages of employees
    impacted relevant to company size.

    Parameters
    ----------
    total_funding_list : list
        List of total fnudings received by companys announcing 
        layoffs.
    percentage_impacted_list : list
        List of percentages of employees impacted per layoff 
        announcement.
    company_size_list : list
        List of sizes of companies announcing layoffs.

    Returns
    -------
    None.

    """
    user_input = -1
    while user_input != 0:
        print("""
 Menu:  
 1. Display Analysis of Percentages of Employees Impacted
    with Relevance to Company Size.
 2. Display Pie-Chart Representing Distribution of Layoff
    Announcements per Company Size.
 3. Display Multiple Bar Chart of Average Percentages of
    Employees Impacted Versus Company Size.
 4. Display Multiple Box-Plot of Average Percentages of
    Employees Impacted Versus Company Size.
        """)   
        user_input = input(sub_menu_prompt)
        try:
           user_input = int(user_input)
        except:
           print("Invalid entry")
           continue
        if int(user_input) == 1:
           # Display subcategory analysis of percentage of employees impacted per company size
           display.display_subcategory_analysis(analyse.analyse_subcategory(company_size_list, percentage_impacted_list))
        elif int(user_input) == 2:
            # Pie-chart of layoff announcements per company size
            visualise.announcements_per_size_pie_chart(company_size_list, percentage_impacted_list)
        elif int(user_input) == 3:
            # Bar-chart of average % impacted per company size
            visualise.avg_percentage_impacted_per_size_bar_chart(company_size_list, percentage_impacted_list)
        elif int(user_input) == 4:
            # Box-plots of % impacted per company size
            visualise.avg_percentage_impacted_per_size_box_plots(company_size_list, percentage_impacted_list)   
        elif user_input == 0:
            break
        else:
            print("Invalid entry")
    return
   
def home_menu(company_size_list, total_funding_list, percentage_impacted_list):
    """
    Display user menu for navigating sections of analysis report.

    Parameters
    ----------
    total_funding_list : list
        List of total fnudings received by companys announcing 
        layoffs.
    percentage_impacted_list : list
        List of percentages of employees impacted per layoff 
        announcement.
    company_size_list : list
        List of sizes of companies announcing layoffs.

    Returns
    -------
    None.

    """
    home_prompt = "Please select an option from the menu: (0 to exit): "
    user_input = -1
    while user_input != 0:
        print("""
US Tech Layoff Announcements in 2022
      
Home Menu:
1. Analysis of Total Funding Recieved per Company.
2. Analysis of Percentages of Employees Impacted.
3. Correlation Between Total Funding Recieved per Company 
   and Percentages of Employees Impacted.
4. Analysis of Percentages of Employees Impacted Related
   to Company Size.
        """)
        user_input = input(home_prompt)
        try:
           user_input = int(user_input)
        except:
           print("Invalid entry")
           continue
        if user_input == 1:
            total_funding_menu(total_funding_list)
        elif user_input == 2:
            percentage_impacted_menu(percentage_impacted_list)
        elif user_input == 3:
            correlation_menu(total_funding_list, percentage_impacted_list)
        elif user_input == 4:
            analysis_by_company_size_menu(total_funding_list, percentage_impacted_list, company_size_list)
        elif user_input == 0:
            sys.exit()
        else:
            print("Invalid entry")
