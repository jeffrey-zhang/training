package main

import "unicode/utf8"

var (
	b int32 = 123
	c       = 456
	d       = "hello"
	e       = 12.3
)

func main() {
	println("hello go")

	str1 := "你好 124"
	println(len(str1))
	println(utf8.RuneCountInString(str1))

}
