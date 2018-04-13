def check_phone(phone):
	if phone.startswith("1") and len(phone)==11:
		print("手机号码是正确的")
	else:
		print("手机号是错的")

#第一个功能
phone = input("请输入手机号")
check_phone(phone)

#另一个功能
phone2 = input("请输入手机号")
check_phone(phone)
