# impliment a linked list and its operations
# add node, delete node, get count, display linked list

class Node:
	def __init__(self, data, node=None):
		self.data = data
		self.next = node

	def __str__(self):
		return(f"<LinkedListNode:{self.data}>")

class LinkedList:

	def __init__(self):
		self.head = None
		self.count = 0

	def add_node(self, data):
		new_node = Node(data)
		
		if self.head == None:
			self.head = new_node
		else:
			last_node = self.head
			while(last_node.next != None):
				last_node = last_node.next
			last_node.next = new_node

		print(f"added new node {new_node}")
		self.count += 1



	def get_node(self, position):
		pass

	def update_node(self, position):
		pass

	def delete_node(self, data):
		if self.head.data == data:
			self.head = self.head.next
		else:
			temp = self.head.next
			while temp.next != None:
				if temp.data == data:
					temp = self.head
					if temp.data == data:
						self.head = temp.next
						break
				else:
					temp = temp.next


	def get_list(self):
		temp = self.head
		output = str()
		while True:
			output += temp.__str__()
			temp = temp.next
			if temp == None:
				break
		
		output = output + ' | count : ' + str(self.count)
		print(output)

def main():
	ll = LinkedList()
	ll.add_node(35)
	ll.add_node(49)
	ll.add_node(35)
	ll.add_node(29)
	ll.add_node(15)
	ll.add_node(90)
	ll.get_list()
	ll.delete_node(90)
	ll.get_list()
	ll.delete_node(90)
	ll.get_list()

if __name__ == '__main__':
	main()