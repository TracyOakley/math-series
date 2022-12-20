import pytest
from series.series import fibonacci
from series.series import lucas
from series.series import sum_series

def test_1():
    assert fibonacci

def test_fib_0():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fib_1():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fib_2():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fib_3():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected

def test_fib_4():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected


#**********************************************************

def test_lucas():
    assert lucas

def test_lucas_0():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_lucas_1():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_lucas_2():
    actual = lucas(2)
    expected = 3
    assert actual == expected

def test_lucas_3():
    actual = lucas(3)
    expected = 4
    assert actual == expected

def test_lucas_4():
    actual = lucas(4)
    expected = 7
    assert actual == expected


#**********************************************


def test_sum_series():
    assert sum_series


def test_sum_series_0():
    actual = sum_series(0)
    expected = 0
    assert actual == expected


def test_sum_series_1():
    actual = sum_series(1)
    expected = 1
    assert actual == expected


def test_sum_series_2():
    actual = sum_series(2)
    expected = 1
    assert actual == expected


def test_sum_series_3():
    actual = sum_series(3)
    expected = 2
    assert actual == expected


def test_sum_series_021():
    actual = sum_series(0, 2, 1)
    expected = 2
    assert actual == expected

