def sum(a,b,*args,**kwargs):
	all_sum+=a
	all_sum= all_sum+a
	print(all_sum)



t = (3,4,5)
d = {"date":6}
sum(1,2,*t,**d)
