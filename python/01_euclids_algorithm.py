# calculate thwe GCD of two numbers

def gcd(a: int, b: int)-> int:	
	while( b != 0):
		# back up the value of a
		t = a
		a = b
		b = t % a
	return a

if __name__ == '__main__':
	res = gcd(144, 8)
	print(f"gcd is : {res}")
	res = gcd(60, 96)
	print(f"gcd is : {res}")
	res = gcd(20, 8)
	print(f"gcd is : {res}")
