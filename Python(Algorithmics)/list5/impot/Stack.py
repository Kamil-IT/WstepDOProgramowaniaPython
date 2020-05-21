""" This is my modified code from the lecture material: http://users.uj.edu.pl/~ufkapano/algorytmy/lekcja09/slist2.html """


class Node:
	"""Class representing a node of a stack"""

	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

	def __str__(self):
		return str(self.data) # generic


class Stack:
	"""Class representing a stack"""

	def __init__(self):
		self.length = 0
		self.head = None

	def __str__(self):
		if self.empty() == False:
			node = self.head
			for i in range(self.length):
				print(f'Node {i+1}: {node}')
				node = node.next
			return ''
		else:
			return 'Stos jest pusty'

	def __len__(self):
		return self.length

	def copy(self):
		return self

	def empty(self):
		return self.length == 0

	def push(self, data):
		node = Node(data)
		if self.empty():
			self.head = node
		else:
			node.next = self.head
			self.head = node
		self.length += 1

	def pop(self):
		if self.empty():
			raise ValueError('Stos jest pusty')
		node = self.head
		node_data = node.data
		if self.head.next == None: # self.length == 1
			self.head = None
		else:
			self.head = self.head.next
		node.next = None # clearing connection
		self.length -= 1
		return node_data
