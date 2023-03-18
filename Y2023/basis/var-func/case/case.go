package _case

import "errors"

func SumCase(a, b int) (sum int, err error) {
	if a <= 0 && b <= 0 {
		err = errors.New("两数相加不能同时小于0")
		return
	}

	sum = a + b
	return
}

func ReferenceCase(a int, b *int) {
	a += 1
	*b += 1
}

var g int
var G int

func ScopeCase(a, b int) {
	c := 100
	g = a + b + c
	G = g
}


//面向对象
type User struct {
	Name string
	Age  int
}

func NewUser(name string, age int) *User {
	return &User{Name: name, Age: age}
}

func (u *User) GetName() string {
	return u.Name
}

func (u *User) GetAge() int {
	return u.Age
}
