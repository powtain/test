package main

// BubbleSort returns a new slice sorted in ascending order using bubble sort.
// The input slice is not modified.
func BubbleSort(nums []int) []int {
	result := append([]int(nil), nums...)
	n := len(result)
	if n < 2 {
		return result
	}

	for i := 0; i < n-1; i++ {
		swapped := false
		for j := 0; j < n-1-i; j++ {
			if result[j] > result[j+1] {
				result[j], result[j+1] = result[j+1], result[j]
				swapped = true
			}
		}
		if !swapped {
			break
		}
	}

	return result
}
