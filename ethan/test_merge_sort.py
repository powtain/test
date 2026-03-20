"""Tests for merge sort implementation."""

from ethan.merge_sort import merge_sort


def test_merge_sort_sorts_numbers_ascending() -> None:
    values = [5, 2, 4, 6, 1, 3]

    result = merge_sort(values)

    assert result == [1, 2, 3, 4, 5, 6]


def test_merge_sort_handles_empty_list() -> None:
    assert merge_sort([]) == []


def test_merge_sort_handles_single_element() -> None:
    assert merge_sort([1]) == [1]


def test_merge_sort_handles_already_sorted() -> None:
    values = [1, 2, 3, 4, 5]

    result = merge_sort(values)

    assert result == [1, 2, 3, 4, 5]


def test_merge_sort_handles_reverse_sorted() -> None:
    values = [5, 4, 3, 2, 1]

    result = merge_sort(values)

    assert result == [1, 2, 3, 4, 5]
