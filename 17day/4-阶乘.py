#5! = 5*4*3*2*1
#4! = 4*3*2*1
#3! = 3*2*1

num = 1
result = 1
while num <=5:
	#result = result*num
	result*=num

	num+=1

print(result)
#5! = 5*4!
#4! = 4*3!

def xxxx(num):
	#3! = 3*2!
	num*xxxxx(num-1)	

def xxx(num):
	#4*3!
	#num*xxxx(num-1)
	#4*xxxx(3)
def get_num(num):
	if num == 1:
		return 1
	else:
		return num*get_num(num-1)
	#5*4!
	#5*xxx(num-1)
	#num*get_num(num-1)


get_num(5)
"""
return 5*get_num(5-1)
return 4*get_num(4-1)
return 3*get_num(3-1)
return 2*get_num(2-1)
return 1
5*4*3*2*1
"""
