# A class that represents an individual node in a
class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key


# A function to do inorder tree traversal
def printInorder(root):

	if root:

		# First recur on left child
		printInorder(root.left)

		# Then print the data of node
		print(root.val, end=" ")

		# Now recur on right child
		printInorder(root.right)



# A function to do inorder tree traversal
def printPreorder(root):

	if root:

		# Then print the data of node
		print(root.val, end=" ")

		# First recur on left child
		printPreorder(root.left)

		# Now recur on right child
		printPreorder(root.right)


# A function to do inorder tree traversal
def printPostorder(root):

	if root:

		# Then print the data of node
		print(root.val, end=" ")

		# First recur on left child
		printPostorder(root.left)

		# Now recur on right child
		printPostorder(root.right)


# Driver code
if __name__ == "__main__":
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.right.left = Node(6)
	root.right.right = Node(7)

	# Function call
	print("Inorder traversal of binary tree is")
	printInorder(root)
	print()
	printPreorder(root)
	print()
