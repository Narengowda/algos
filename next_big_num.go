package main

import "fmt"

// Given an array A [  ] having distinct elements,
// the task is to find the next greater element for each element
// of the array in order of their appearance in the array.

func main() {

	x := []int{1, 3, 2, 4, 1, 2, 7, 8, 6, 5, 9}
	fmt.Println("input")
	fmt.Println(x)

	output := make([]int, 0)
	var latest_high int

	for _, ele := range x {

		if ele > latest_high {
			latest_high = ele
		}
		output = append(output, latest_high)
	}

	output = append(output, -1)
	fmt.Println("output")
	fmt.Println(output)

}
