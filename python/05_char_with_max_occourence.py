# find the character that occoures maximum number of times in a string

def max_occourence(sent:str=None) -> str | None:
	if sent is None:
		return None

	count = dict()

	for chr in sent:
		if chr in count:
			count[chr] += 1
		else:
			count[chr] = 1

	return max(count, key=count.get)

def main():
	sent = 'geeks for geeks'
	res = max_occourence(sent)
	print(f'character that occoures max number of times is : {res}')

if __name__ == '__main__':
	main()