num  = 10
def test(num):
	#num+=num
	num = num+num
	print(num)

a = [100]
def test1(a):
	# python按引用传值
	#a+=a是把算好的值给已经有引用的
	#a=a+a 先算右边.复制一个新的变量
	#a+=a
	a = a+a
	print(a)

test(num)
print(num)

test1(a)
print(a)


