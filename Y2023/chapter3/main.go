package main

import "fmt"

type myInt int

func main() {
	var a int = 1
	var b myInt = 2
	fmt.Println(a + int(b))

	const(
		c = 5
		d = 3.1415926
	)
	var f  = c + d
	fmt.Println(f)
	fmt.Println("------------")
	const(
		Sunday = 1 >> iota
		Monday 
		Tuesday = 20
		Wed
		Thur = 21 + iota
		Fri
		Sat
	)
	fmt.Println(Sunday)
	fmt.Println(Monday)
	fmt.Println(Tuesday)
	fmt.Println(Wed)
	fmt.Println(Thur)
	fmt.Println(Fri)
	fmt.Println(Sat)
}