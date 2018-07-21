package main

import "fmt"

func main() {
	input := []int{1, 1, 1, 1, 1, 2, 4, 4, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1}

	sum_array := make([]int, 0)
	sum := 0

	// Evaluate sum array
	for _, i := range input {
		sum = sum + i
		sum_array = append(sum_array, sum)
	}

	// Find the equilibrium point
	var sum_half int = sum / 2
	for j, i := range sum_array {
		if i == sum_half {
			fmt.Println("Found equilibrium point at index = ", j)
			break
		}
	}

}
