"""Tests for insertion sort implementation."""

from ethan.insertion_sort import insertion_sort


def test_insertion_sort_sorts_numbers_ascending() -> None:
    values = [5, 2, 4, 6, 1, 3]

    result = insertion_sort(values)

    assert result == [1, 2, 3, 4, 5, 6]


def test_insertion_sort_handles_empty_list() -> None:
    assert insertion_sort([]) == []
