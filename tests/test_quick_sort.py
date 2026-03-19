from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from ethan.quick_sort import quick_sort


def test_quick_sort_sorts_unsorted_values_without_mutating_input() -> None:
    values = [5, 1, 4, 2, 3]

    result = quick_sort(values)

    assert result == [1, 2, 3, 4, 5]
    assert values == [5, 1, 4, 2, 3]


def test_quick_sort_handles_boundary_inputs() -> None:
    assert quick_sort([]) == []
    assert quick_sort([7]) == [7]


def test_quick_sort_handles_duplicates_and_negative_values() -> None:
    values = [3, -1, 3, 2, 0, -1]

    result = quick_sort(values)

    assert result == [-1, -1, 0, 2, 3, 3]
