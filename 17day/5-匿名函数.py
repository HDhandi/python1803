fun = lambda a,b:a+b
print(fun(1,2))

fun = lambda a,b=3:a+b
print(fun(1,4))


def test1(a,b):
	return a+b


def test(a,b,fun):
	print(fun(a,b))



test(1,7,test1)
