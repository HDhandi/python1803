#定义函数
def jisuanqi(x,y,fuhao):#形参
	if fuhao == "+":
		z = x+y
		return z
	elif fuhao == "-":
		z = x-y
		return z
	elif fuhao == "*":
		z = x*y
		print("积是%0.2f"%z)
	elif fuhao == "/":
		if y != 0:
			z = x/y 
			print("商是%.02f"%z)
		else:
			print("输入错误")		
#调用
while True:
	x = float(input("请输入一个数字"))
	y = float(input("请在输入一个数字"))
	z = input("请输入一个+-*/")
	result = jisuanqi(x,y,z)#实参
	print(result)





