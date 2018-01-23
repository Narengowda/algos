package main

import "fmt"

// Implement a Queue using 2 stacks

type queue struct {
	// stack
	stack []int
}

func (q *queue) push(val int) {
	q.stack = append(q.stack, val)
}

func (q *queue) pop() int {
	ele := q.stack[0]

	// Temp stack, load all the elements
	// and reload in the same order to base
	q.stack = append(q.stack[:0], q.stack[1:]...)
	// This is simple output of above mentioned step

	return ele
}

func main() {

	var que queue

	que.push(1)
	que.push(2)
	que.push(3)

	fmt.Println("elemenet popped ", que.pop())

	que.push(4)
	que.push(5)

	fmt.Println("elemenet popped ", que.pop())
	fmt.Println("elemenet popped ", que.pop())

}
