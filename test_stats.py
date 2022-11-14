"""
A00304351
Test functions for stats module
"""
import stats

def test_calc_mean():
    assert stats.calc_mean([1,2,3,4,5]) == 3
    assert stats.calc_mean([100,75,23,65,34]) == 59.4
    assert stats.calc_mean([-1, 1]) == 0
    
def test_calc_median():
    assert stats.calc_median([1,2,3,4]) == 2.5
    assert stats.calc_median([100,75,23,65,34]) == 65.0
    assert stats.calc_median([-6, 4, 4, 100]) == 4.0

def test_calc_mode():
    assert stats.calc_mode([-6, 4, 4, 100]) == 4.0
    assert stats.calc_mode([1,2]) == 1.0
    assert stats.calc_mode([-1, 1]) == -1.0

def test_calc_range():
    assert stats.calc_range([1,2,3,4,5]) == 4.0
    assert stats.calc_range([100,75,23,65,34]) == 77.0
    assert stats.calc_range([-20, 20]) == 40

def test_calc_iqr():
    assert stats.calc_iqr([1,2,3,4,5]) == 3.0
    assert stats.calc_iqr([9, 44, 89, 88, 48, 82, 59, 83, 3, 45]) == 39.0
    assert stats.calc_iqr([-1, 1]) == 2.0

def test_calc_std_dev():
    assert stats.calc_std_dev([1,2,3,4,5]) == 1.5811388300841898
    assert stats.calc_std_dev([100,75,2.3,6.5,34]) == 42.840319793390904
    assert stats.calc_std_dev([-1, 5, -10, 1, 33]) == 16.272676485446393
    
def test_calc_median_skewness():
    assert stats.calc_median_skewness([1,2,3,4,5]) == 0.0
    assert stats.calc_median_skewness([100,75,2.3,6.5,34]) == 0.669462789687778
    assert stats.calc_median_skewness([-1, 5, -10, 1, 33, 0]) == 0.8484249752187512
    
def test_calc_mode_skewness():
    assert stats.calc_mode_skewness([1,2,3,4,5]) == 1.2649110640673518
    assert stats.calc_mode_skewness([100,75,2.3,6.5,34]) == 0.9631113913011756
    assert stats.calc_mode_skewness([-1, 5, -10, 1, 33, 0]) == 0.9954853042566681
    
def test_calc_correlation():
    assert stats.calc_correlation([1,2,3,4], [2,4,6,8]) == 1.0
    assert stats.calc_correlation([1,2,3,4], [8,6,4,2]) == -1.0
    assert stats.calc_correlation([1,2,3,4], [1,0,0,1]) == 0