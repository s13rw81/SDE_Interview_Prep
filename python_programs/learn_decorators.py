def outer_function():
	message = 'HI'

	def inner_function():
		print(message)
	return inner_function()


outer_function()