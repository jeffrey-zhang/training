package _case

import "fmt"

func FlowControlCase() {
	ifElseCase(0)
	ifElseCase(1)
	ifElseCase(2)

	forCase()
}

func ifElseCase(a int) {
	if a == 0 {
		fmt.Println("executed if")
	} else if a == 1 {
		fmt.Println("executed else if")
	} else {
		fmt.Println("executed else")
	}
}

func forCase() {
	for i := 0; i < 10; i++ {
		if i == 5 {
			continue
		}
		fmt.Println("forL i=", i)
	}
}