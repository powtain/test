"""Insertion sort implementation."""

from __future__ import annotations


def insertion_sort(values: list[int]) -> list[int]:
    """Return a new list sorted in ascending order using insertion sort."""
    sorted_values = values.copy()

    for idx in range(1, len(sorted_values)):
        current = sorted_values[idx]
        pos = idx - 1

        while pos >= 0 and sorted_values[pos] > current:
            sorted_values[pos + 1] = sorted_values[pos]
            pos -= 1

        sorted_values[pos + 1] = current

    return sorted_values


if __name__ == "__main__":
    sample = [5, 2, 4, 6, 1, 3]
    print(insertion_sort(sample))
