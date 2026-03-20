"""Merge sort implementation."""

from __future__ import annotations


def merge_sort(values: list[int]) -> list[int]:
    """Return a new list sorted in ascending order using merge sort."""
    if len(values) <= 1:
        return values.copy()

    mid = len(values) // 2
    left = merge_sort(values[:mid])
    right = merge_sort(values[mid:])

    return merge(left, right)


def merge(left: list[int], right: list[int]) -> list[int]:
    """Merge two sorted lists into a single sorted list."""
    result: list[int] = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


if __name__ == "__main__":
    sample = [5, 2, 4, 6, 1, 3]
    print(merge_sort(sample))
