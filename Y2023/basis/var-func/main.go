package main

import (
	_case "basis/var-func/case"
	"fmt"
)

func main() {

	a := 10
	b := 20
	fmt.Println(_case.SumCase(a, b))
	fmt.Println("--------")

	_case.ReferenceCase(a, &b)
	fmt.Println(a, b)
	fmt.Println("--------")

	v, err := _case.SumCase(a, b)
	if err == nil {
		fmt.Println(v)
	}
	fmt.Println("--------")

	fmt.Println(_case.G)
	_case.ScopeCase(a, b)
	fmt.Println(_case.G)
	fmt.Println("--------")

	user := _case.NewUser("jeffrey", 18)
	fmt.Println(user.GetName(), user.GetAge())


}
