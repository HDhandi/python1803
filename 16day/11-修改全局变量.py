num = 0

def test():
	global num #你要修改全局变量 
	num = 1
	print(num)

test()
print(num)
