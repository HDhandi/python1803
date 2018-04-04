distance = 73 #距离
money = 0#单次钱数
sum = 0#总钱
i = 1#变量
while i<= 60:
	if  distance <= 6:
		money = 3
	elif distance > 6 and distance <=12:
		money = 4
	elif distance > 12 and distance <=22:
		money = 5
	elif distance > 22 and distance <=32:
		money = 6
	elif distance > 32: 
		if (distance - 32)%20 == 0:
			money = 6 + (distance-32)/20
		else:
			money = 6+ int((distance-32)/20) + 1

	if sum >= 100 and sum < 150: 
		money = money * 0.8
	elif sum>=150 and sum < 400:
		money = money * 0.5


	sum  = sum + money

	i+=1
print("钱是%0.2f"%sum)












