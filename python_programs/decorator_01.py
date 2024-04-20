def logoutput(func):
	def wrapper(*args):
		print('logging output of func')
		res = func()
		print("result of func is ", res)
		return res
	return wrapper
	
def logoutput(func):
	def wrapper(*args):
		print('logging output of func')
		res = func()
		print("result of func is ", res)
		return res
	return wrapper

@logoutput
def main_func(salt=0):
	return salt * 500

if __name__ == '__main__':
	main_func(5)
