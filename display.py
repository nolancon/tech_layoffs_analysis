# display contains functions for displaying data
# in a user-friiendly manner.
import stats

def display_total_funding_data(numbers):
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

def display_correlation(x_numbers, y_numbers)    :
    print(f"Correlation: {stats.calc_correlation(x_numbers, y_numbers):.3f}")
    print()
    
    
def display_subcategory_analysis(percentage_impacted_by_company_size):
    for company_size in percentage_impacted_by_company_size:
        print(str(company_size) + ": " + str(percentage_impacted_by_company_size[company_size]))
    print()