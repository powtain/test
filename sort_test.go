package main

import (
	"slices"
	"testing"
)

func TestBubbleSort(t *testing.T) {
	tests := []struct {
		name string
		in   []int
		want []int
	}{
		{
			name: "nil slice",
			in:   nil,
			want: nil,
		},
		{
			name: "empty slice",
			in:   []int{},
			want: []int{},
		},
		{
			name: "already sorted",
			in:   []int{1, 2, 3, 4, 5},
			want: []int{1, 2, 3, 4, 5},
		},
		{
			name: "reverse order",
			in:   []int{5, 4, 3, 2, 1},
			want: []int{1, 2, 3, 4, 5},
		},
		{
			name: "contains duplicates",
			in:   []int{3, 1, 2, 3, 2},
			want: []int{1, 2, 2, 3, 3},
		},
		{
			name: "contains negative values",
			in:   []int{0, -1, 5, -3, 2},
			want: []int{-3, -1, 0, 2, 5},
		},
	}

	for _, tc := range tests {
		tc := tc
		t.Run(tc.name, func(t *testing.T) {
			input := slices.Clone(tc.in)
			BubbleSort(input)
			if !slices.Equal(input, tc.want) {
				t.Fatalf("BubbleSort(%v) = %v, want %v", tc.in, input, tc.want)
			}
		})
	}
}

func TestBubbleSortSortsInPlace(t *testing.T) {
	input := []int{3, 2, 1}
	alias := input

	BubbleSort(input)

	if !slices.Equal(alias, []int{1, 2, 3}) {
		t.Fatalf("expected alias to observe in-place mutation, got %v", alias)
	}
}
