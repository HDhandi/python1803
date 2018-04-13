"""
这个函数的功能只用来添加英雄
"""

list = []#用来装英雄
def add_hero(hero):
	list.append(hero)

def a():
	if len(list) == 5:
		print(list)
		break

while True:
	a()
	name = input("请输入英雄名字")
	add_hero(name)
