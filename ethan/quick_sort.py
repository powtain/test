from __future__ import annotations

import sys
from typing import Sequence


def quick_sort(values: Sequence[int]) -> list[int]:
    items = list(values)
    if len(items) < 2:
        return items

    pivot = items[len(items) // 2]
    lower = [value for value in items if value < pivot]
    equal = [value for value in items if value == pivot]
    higher = [value for value in items if value > pivot]
    return quick_sort(lower) + equal + quick_sort(higher)


def main(argv: Sequence[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)

    try:
        values = [int(arg) for arg in args]
    except ValueError as error:
        raise SystemExit(f"all arguments must be integers: {error}") from error

    print(quick_sort(values))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
