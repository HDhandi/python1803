#你爸爸让你去买烟，给你20块钱，花了10快，剩下的10块返回给你爸爸


def  buy_smoke(money):
	shengyu = 20-10
	smoke = "云烟"
	return shengyu,smoke #剩余的钱返回给你爸爸


#爸爸让你去买烟,给你了20
qianbao,smoke = buy_smoke(20)
print(qianbao)#爸爸数数钱
print(smoke)	

