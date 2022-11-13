"""
A00304351
Functions for displaying statistics in a user-friiendly manner.
"""

import stats

def display_total_funding_data(numbers):
    """
    Display statistics for total funding received per company
    announcing layoffs.

    Parameters
    ----------
    numbers : list
        List of total fundings received by companies annonucing
        layoffs.

    Returns
    -------
    None.

    """
    print("Total Funding Received ($)")
    print("Number of Values:", len(numbers))
    print("Total:", sum(numbers))
    print(f"Mean (average): {stats.calc_mean(numbers):.3f}")
    print("Median:", stats.calc_median(numbers))
    print("Mode:", stats.calc_mode(numbers))
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))
    print("Range:", stats.calc_range(numbers))
    print("Inter-Quartile Range:", stats.calc_iqr(numbers))
    print(f"Standard Deviation: {stats.calc_std_dev(numbers):.3f}")
    print(f"Median Skewness: {stats.calc_median_skewness(numbers):.3f}")
    print(f"Mode Skewness: {stats.calc_mode_skewness(numbers):.3f}")
    print()
 
def display_percentage_impacted_data(numbers):
    """
    Display statistics for percentages of employees impacted
    per company announcing layoffs.

    Parameters
    ----------
    numbers : list
        Lsit of percentages of employees impacted by company 
        announcing layoffs.

    Returns
    -------
    None.

    """
    print("Percentage of Employees Impacted per Company")
    print("Number of Values:", len(numbers))
    print(f"Mean (average): {stats.calc_mean(numbers):.3f}")
    print("Median:", stats.calc_median(numbers))
    print("Mode:", stats.calc_mode(numbers))
    print("Maximum:", max(numbers))
    print(f"Minimum: {min(numbers):.3f}")
    print(f"Range: {stats.calc_range(numbers):.3f}")
    print("Inter-Quartile Range:", stats.calc_iqr(numbers))
    print(f"Standard Deviation: {stats.calc_std_dev(numbers):.3f}")
    print(f"Median Skewness: {stats.calc_median_skewness(numbers):.3f}")
    print(f"Mode Skewness: {stats.calc_mode_skewness(numbers):.3f}")
    print()

def display_correlation(x_numbers, y_numbers):
    """
    Display correlation between x_numbers and y_numbers.

    Parameters
    ----------
    x_numbers : list
        List of statistical numbers.
    y_numbers : list
        List of statistical numbers.

    Returns
    -------
    None.

    """
    print(f"Correlation: {stats.calc_correlation(x_numbers, y_numbers):.3f}")
    print()
    
    
def display_subcategory_analysis(percentage_impacted_by_company_size):
    """
    Display analysis of percentages of employees impacted subcategorised
    by cmpany size.

    Parameters
    ----------
    percentage_impacted_by_company_size : dictionary
        Dictionary of data accumulated on percenatages of employees impacted
        by layoffs based on company size.

    Returns
    -------
    None.

    """
    for company_size in percentage_impacted_by_company_size:
        print(str(company_size) + ": " + str(percentage_impacted_by_company_size[company_size]))
    print()