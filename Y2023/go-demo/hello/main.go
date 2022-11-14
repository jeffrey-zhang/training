package main


func main(){
	data := []int{10,11,12}
	for i := range data{
		println(i)
	}

	for _, v:= range data{
		println(v)
	}
	
	for range data{
		println("a")
	}

	for i, v := range data{
		println(i, v)
	}
}