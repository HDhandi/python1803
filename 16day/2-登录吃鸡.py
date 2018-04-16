#注册
#isphone("")
def register(phone,pwd):
	result = isPhone(phone)
	if result:
		print("注册成功")
	else:
		print("注册失败")
#登录
def login(phone,pwd):
	result = isPhone(phone)
	if result:
		print("登录成功")
	else:
		print("登录失败")

def isPhone(phone):
	if phone.startswith("1") and len(phone) == 11:
		return True
	else:
		return False	
#isphone("12347435")
"""
def xxx():
	#xxxxx

def xxxxx():
	#xxxx

def xxxx():
	#xxxx
"""
register("16778901234","123456")
login("16778901234","123456")








