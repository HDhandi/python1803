list = [5,23,1,3,67,7,32]


for i in range(len(list)):
	for j in range(i+1,len(list)):
		if list[i]> list[j]:
			list[i],list[j] = list[j],list[i]


print(list)



