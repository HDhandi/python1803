list = [1,2]

def test():
	global list
	list.append(3)
	print(list)



test()
print(list)
