import time
def play_game():
	for i in range(10):
		print("玩吃鸡 哒哒哒哒")
		time.sleep(1)
	print("你爸爸来了")
	result = kill()
	if result =="削死了":
		print("game over")
	else:
		print("go on play game")
	

def kill():
	print("一顿削")
	return "削惨了"


play_game()
