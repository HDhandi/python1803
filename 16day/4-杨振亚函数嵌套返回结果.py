import time
def up_class():
	print("杨振亚正在听课")
	result = call_phone()
	if result != "有事":
		print("杨振亚继续上课")
	else:
		print("出去了出去了")
def call_phone():
	for i  in range(10):
		print("杨振亚接电话")
		time.sleep(1)
	return "有事"	

up_class()
