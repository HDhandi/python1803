students = []#学生列表，里面是每个学生的三个成绩
MaxSumGrade = 0#用来记录总分最大值
position = 0#用来记录总分最大值的索引
def input_garde():#用来输入成绩
	for i in range(5):#用来输入5名学生
		print("第%d名学生"%(i+1))#用来打印第几名学生
		global MaxSumGrade#用global声明要修改全局变量
		grade_list = []#用来记录一名学生的三科成绩
		for j in range(3):#用来输入3科成绩
			grade = float(input("请输入成绩"))#用来输入成绩
			grade_list.append(grade)#加入到列表

		students.append(grade_list)#把三科成绩的列表加入到学生列表
		if sum(grade_list) > MaxSumGrade:#判断是不是总分最大值 第一次一定是大于恒满足
			MaxSumGrade = sum(grade_list)#把总分最大值记录下来，覆盖上次总分最大值
			position = i #记录总分最大值的所在的索引

	print("最高总分为%0.2f"%MaxSumGrade)#输入总分最大值
	print("成绩分别为%0.2f分 %0.2f分 %0.2f分"%(students[position][0],students[position][1]
	,students[position][2]))#根据索引输出总分最大的是单科成绩
	print("平均分为%0.2f分"%(MaxSumGrade/3))#总分最大除以科目数等于平均分,可以不保留两位小数


input_garde()#调用函数

















