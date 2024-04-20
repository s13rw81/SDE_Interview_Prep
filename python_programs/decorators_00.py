def deco(func):
	def wrapper(*args):
		print('before running func')
		res = func(*args)
		print('after running func')
		return res
	return wrapper

@deco
def multiple(a):
	return a * a

if __name__ == '__main__':
	res = multiple(5)
	print(res)