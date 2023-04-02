package _case

import "fmt"

func SimpleCase() {
	a, b := 3, 4
	c, d := 5.0, 6.0
	fmt.Println(getMaxNum(a, b))
	fmt.Println(getMaxNum(c, d))
}

func getMaxNumInt(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func getMaxNumFloat(a, b float32) float32 {
	if a > b {
		return a
	}
	return b
}

func getMaxNum[T int | float64](a, b T) T {
	if a > b {
		return a
	}
	return b
}
