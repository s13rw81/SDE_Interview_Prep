def fibbonacci_at_n(n: int, memo: dict = {}):
	print(memo)
	if n in memo: return memo[n]

	# calculate nth fibbonacci number
	if n <= 2:
		return 1
	else:
		memo[n] = fibbonacci_at_n(n - 1) + fibbonacci_at_n(n - 2)
		return memo[n]

def main():
	n = 22
	res = fibbonacci_at_n(n)
	print(f"fibbonacci number at {n} is {res}")


if __name__ == '__main__':
	main()