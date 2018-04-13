#定义函数
#这个函数的功能只计算传的值，把计算好的结果返回给我,打印不打印函数不要考虑了
def  jisuanqi(x,y,fuhao):#形参
	if fuhao == "+":
		z = x+y
	elif fuhao == "-":
		z = x-y
	elif fuhao == "*":
		z = x*y
	elif fuhao == "/":
		if y != 0:
			z = x/y 
		else:
			return "输入错误"
	return z		
#调用
while True:
	x = float(input("请输入一个数字"))
	y = float(input("请在输入一个数字"))
	z = input("请输入一个+-*/")
	result = jisuanqi(x,y,z)#实参
	print(result)





