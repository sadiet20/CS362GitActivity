'''
Sadie Thomas
CS 362 - Git in class activity
4/15/21
'''

def calc(a, b):
	sum = a+b
	print("sum =", sum)
	dif = a-b
	print("dif =", dif)
	mul = a*b
	print("mul =", mul)
	div = a/b
	print("div =", div)
	my_list = [sum, dif, mul, div]
	print(my_list)
	add = 0
	for i in range(4):
		add += my_list[i]
	print("sum of the list =", add)

calc(3, 4)
