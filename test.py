
def hasDuplicates(array1, array2):

	contains = {}

	for item in array1:
		contains[item] = True

	for item in array2:
		if item in contains:
			return True

	return False


print(hasDuplicates([1, 2, 3], [4, 5, 8]))


def hasDuplicates2(array1, array2):
	# combined = array1 + array2
	# filtered = set(combined)

	# if len(combined) > len(filtered):
	# 	return True
	# else:
	# 	return False

	return True if len(array1 + array2) > len(set(array1 + array2)) else False

print(hasDuplicates2([1, 2, "a"], [4, "b", 8]))



array = [1, 3, 9, 8]
array2 = [1, 5, 4, 6]
array3 = [0, 0, 0, 0]
num = 10

def hasSumOfTwo(array, num):
	compliments = []

	for i in array:
		if i in compliments:
			return True
		compliments.append(num - i)

	return False

print(hasSumOfTwo(array2, num))


def reverseStr(string):
	out = ""

	for i in range(len(string), 0, -1):
		out += string[i-1]

	return out

print(reverseStr("hello"))


def mergeSortedArrays(arr1, arr2):
	return sorted(arr1 + arr2)

print(mergeSortedArrays([1,3,9,4,7], [5, 3, 7]))


nums = [1,2,3,4,5,6,7, 8, 9]
k = 6

def rotateList(k, nums):
	for i in range(k):
	    nums.insert(0, nums[-1])
	    nums.pop(-1)


nums = [0,1,0,3,12]

def moveZeros(nums):
	for i in range(len(nums) -1, -1, -1):
		if nums[i] == 0:
			nums.pop(i)
			nums.append(0)



nums = [-2,-1,-3, -4,-1,-2,-1,-5,-4]

def maxSubArray(nums):

	maxSum = nums[0]
	curSum = 0

	for i in nums:
		if curSum < 0:
			curSum = 0
		curSum += i

		if curSum > maxSum:
			maxSum = curSum

	return maxSum

print(maxSubArray(nums))



a=[-1, 0, 1,3,4,6,20]
b=[4,20]

def mergeSortedArrays(a, b):
	
	a.append(None)
	b.append(None)

	i = 0
	j = 0

	new = []
	while True:
		if a[i] != None and b[j] != None:
			if a[i] > b[j]:
				new.append(b[j])
				j += 1
			else:
				new.append(a[i])
				i += 1
		else:
			if a[i] != None:
				new.append(a[i])
				i += 1
			elif b[j] != None:
				new.append(b[j])
				j += 1

		if a[i] == None and b[j] == None:
			break

	print(new)

mergeSortedArrays(a, b)


def func(lst):
	l = []

	for i in lst:
		if i in l:
			return i
		l.append(i)

print(func([2,3,4,5]))


def func(lst):
	l = {}

	for i in lst:
		if i in l:
			return i
		l[i] = True

print(func([2,2,3,3,2,4,5]))


class hashTable():
	def __init__(self, size):
		self.data = [None] * size

	def __hash__(self, key, length = None):
		hash = 0
		key = str(key)
		if not length:
			length = len(self.data)
		for i in range(len(key)):
			hash = (hash + ord(key[i]) * i) % length
		return hash

	def __keyIndexLink__(self, address, key):
		for i in range(len(self.data[address])):
			if self.data[address][i][0] == key:
				return i
		return None

	def set(self, key, value):
		address = self.__hash__(key)
		if not self.data[address]:
			self.data[address] = [[key, value]]
		else:
			index = self.__keyIndexLink__(address, key)
			if index != None:
				self.data[address][index][1] = value
			else:
				self.data[address].append([key, value])

	def get(self, key):
		address = self.__hash__(key)
		if len(self.data[address]) == 1:
			return self.data[address][0][1]
		else:
			index = self.__keyIndexLink__(address, key)
			if index != False:
				return self.data[address][index][1]

	def keys(self):
		lst = []
		for i in self.data:
			if i == None:
				continue
			if len(i) > 1:
				for j in i:
					lst.append(j[0])
			else:
				lst.append(i[0][0])
		return lst


tbl = hashTable(50)
tbl.set("hello", "hey there")

print(tbl.keys())
print(tbl.get("hello"))
print(tbl.__hash__("hello"))

import math
class node():
	def __init__(self, value, doubly = False):
		self.value = value
		self.next = None
		if doubly:
			self.prev = None

class linkedList():
	def __init__(self, value, doubly = False):
		self.doubly = doubly
		self.head = node(value, doubly)
		self.tail = self.head
		self.length = 1

	def append(self, value):
		newNode = node(value, self.doubly)
		if self.doubly:
			newNode.prev = self.tail
		self.tail.next = newNode
		self.tail = newNode
		self.length += 1

	def prepend(self, value):
		newNode = node(value, self.doubly)
		if self.doubly:
			self.head.prev = newNode
		newNode.next = self.head
		self.head = newNode
		self.length += 1

	def values(self):
		values = []

		currentNode = self.head
		for _ in range(self.length):
			values.append(currentNode.value)
			currentNode = currentNode.next
		return values

	def insert(self, value, index):
		if index > self.length :
			raise Exception(f"Index out of range. Last index is {self.length}")
		elif index < 0:
			raise Exception("Can't have negative numbers as an index")
		elif index == 0:
			self.prepend(value)
			return
		elif index == self.length:
			self.append(value)
			return

		currentNode = self.head
		for i in range(self.length):
			if i == index - 1:
				newNode = node(value)
				if self.doubly:
					newNode.prev = currentNode
					currentNode.next.prev = newNode
				newNode.next = currentNode.next
				currentNode.next = newNode
				self.length += 1
				break

			currentNode = currentNode.next

	def find(self, value, all = False):
		indexes = []

		currentNode = self.head
		for i in range(self.length):
			if currentNode.value == value:
				indexes.append(i)
				if not all:
					break
			currentNode = currentNode.next

		return indexes

	def remove(self, index):

		if index > self.length - 1:
			raise Exception(f"Index out of range. Last index is {self.length - 1}")
		elif index == 0:
			self.head = self.head.next
			if self.doubly:
				self.head.prev = None
			self.length -= 1
		elif index < 0:
				raise Exception("Can't have negative numbers as an index")

		end = False
		if index >= math.floor(self.length / 2):
			end = True

		if end and self.doubly:
			currentNode = self.tail

			for i in range (self.length -1, 1, -1):
				if index + 1 == i:
					currentNode.prev.prev.next = currentNode
					currentNode.prev = currentNode.prev.prev
					self.length -= 1
					break
				currentNode = currentNode.prev

		else:
			currentNode = self.head

			for i in range(self.length - 1):
				if index - 1 == i:
					currentNode.next = currentNode.next.next
					self.length -= 1
					break
				currentNode = currentNode.next

	def removeValue(self, value, all = False):
		lastNode = None
		currentNode = self.head
		valueRemoved = False

		while currentNode != None:
			if self.head.value == value:
				self.head = self.head.next
				if self.doubly:
					self.head.prev = None
				self.length -= 1
				valueRemoved = True

			elif currentNode.value == value:
				lastNode.next = currentNode.next
				if self.doubly:
					currentNode.next.prev = lastNode
				self.length -= 1
				valueRemoved = True

			if valueRemoved and all == False:
				break
			lastNode = currentNode
			currentNode = currentNode.next

	def reverse(self):
		if self.head.next == None:
			return

		lastNode = self.head
		currentNode = lastNode.next
		for _ in range(self.length):
			if currentNode == None:
				break

			nextNode = currentNode.next
			if self.doubly:
				currentNode.prev = nextNode
				lastNode.prev = currentNode

			currentNode.next = lastNode
			lastNode = currentNode
			currentNode = nextNode
			if nextNode == None:
				break
			currentNode = nextNode

		self.head.next = None
		self.tail = self.head
		self.head = lastNode

lst = linkedList(10, True)
lst.append(5)
lst.append(4)
lst.append(3)
lst.append(2)
lst.append(1)
lst.append(0)
lst.prepend(11)
print(lst.values())
lst.insert(19, 3)
lst.remove(7)
print(lst.values())


class node():
	def __init__(self, value):
		self.value = value
		self.next = None

class stack():
	def __init__(self, value = None):
		self.top = node(value)
		if self.top.value == None:
			self.length = 0
		else:
			self.length = 1

	def push(self, value):
		if self.top.value == None:
			self.top.value = value
			self.length += 1
			return

		newNode = node(value)
		newNode.next = self.top
		self.top = newNode
		self.length += 1

	def peek(self):
		return self.top.value

	def pop(self):
		if self.top.value == None:
			raise Exception("Stack is empty")

		value = self.top.value
		if self.top.next != None:
			self.top = self.top.next
			self.length -= 1
		else:
			self.top.value = None
			self.length -= 1
		return value

class node():
	def __init__(self, value):
		self.value = value
		self.next = None

class queue():
	def __init__(self, value = None):
		self.first = node(value)
		self.last = self.first
		if value == None:
			self.length = 0
		else:
			self.length = 1

	def peek(self):
		return self.first.value

	def enqueue(self, value):
		if self.first.value == None:
			self.first.value = value
			self.length += 1
		else:
			newNode = node(value)
			self.last.next = newNode
			self.last = newNode
			self.length += 1

	def dequeue(self):
		if self.first.value == None:
			raise Exception("Queue empty")
		elif self.first.next == None:
			self.first.value = None
			self.length -= 1
		else:
			self.first = self.first.next
			self.length -= 1



class queueStack:

	def __init__(self):
	    self.stack1 = stack()
	    self.stack2 = stack()
	
	def stackToStack(self, fromStack, toStack):
		for _ in range(fromStack.length):
			toStack.push(fromStack.pop())

	def push(self, value):
		self.stackToStack(self.stack1, self.stack2)
		self.stack1.push(value)
		self.stackToStack(self.stack2, self.stack1)

	def pop(self):
		return self.stack1.pop()

	def peek(self):
		return self.stack1.peek()

	def empty(self):
		return True if self.stack1.length == 0 else False



class node():
	def __init__(self, value = None):
		self.value = value
		self.left = None
		self.right = None


class binaryTree():
	def __init__(self):
		self.root = node()

	def insert(self, value):
		if self.root.value == None:
			self.root.value = value
			return

		currentNode = self.root
		while currentNode:
			if currentNode.value == value:
				break

			elif currentNode.value > value:
				if currentNode.left != None:
					currentNode = currentNode.left
				else:
					newNode = node(value)
					currentNode.left = newNode
					break

			elif currentNode.value < value:
				if currentNode.right != None:
					currentNode = currentNode.right
				else:
					newNode = node(value)
					currentNode.right = newNode
					break

	def lookup(self, value):
		if self.root.value == None:
			return False

		currentNode = self.root
		while currentNode:
			if currentNode.value == value:
				return True

			elif currentNode.value > value:
				if currentNode.left == None:
					return False
				else:
					currentNode = currentNode.left

			elif currentNode.value < value:
				if currentNode.right == None:
					return False
				else:
					currentNode = currentNode.right

	def remove(self, value):
		if self.root.value == None:
			return

		currentNode = self.root
		lastNode = None
		while currentNode:
			if currentNode.value == value:
				if currentNode.right == None:
					if lastNode == None:
						currentNode = currentNode.left
						break
					else:
						lastNode.right = currentNode.left
						break
				elif currentNode.right != None:
					if currentNode.right.left == None:
						currentNode.value = currentNode.right.value
						currentNode.right = currentNode.right.right
						break
					else:
						leftNode = currentNode.right.left
						lastLeftNode = None
						while leftNode:
							if leftNode.left == None:
								currentNode.value = leftNode.value
								lastLeftNode.left = leftNode.right
								break
							lastLeftNode = leftNode
							leftNode = leftNode.left
			elif currentNode.value > value:
				lastNode = currentNode
				currentNode = currentNode.left
			elif currentNode.value < value:
				lastNode = currentNode
				currentNode = currentNode.right


class graph():
	def __init__(self):
		self.nodes = 0
		self.adjList = {}

	def addVertex(self, node):
		if node in self.adjList:
			raise Exception("Node already in graph")

		self.adjList[node] = []
		self.nodes += 1

	def addEdge(self, node1, node2):
		if node1 not in self.adjList:
			self.addVertex(node2)
		if node2 not in self.adjList:
			self.addVertex(node2)

		self.adjList[node1].append(node2)
		self.adjList[node2].append(node1)

	def showConnections(self):
		keys = self.adjList.keys()
		out = ""
		for i in keys:
			txt = f"{i} is connected to - "
			for j in self.adjList[i]:
				txt += f"{j},"
			out += (f"{txt[:len(txt) - 1]}\n")
		return out


def factorialRecursive(num):
	if num == 2:
		return 2
	return num * factorialRecursive(num - 1)

def factorialIterative(num):
	total = num * (num - 1)
	for i in range(num - 2, 1, -1):
		total *= i
	return total


def fibb(n):
	if n <= 1:
		return n
	return fibb(n-1) + fibb(n-2)

def fibbIter(n):
	num = [0, 1]
	for i in range(2, n+1, 1):
		num.append((num[i-2] + num[i-1]))
	return num[-1]

print(fibbIter(5))


[0,1,2,3,4,5,6,7,8]
[0,1,1,2,3,5,8,13,21]
def fibb(n, nums = [0, 1]):
	if n == 0:
		return nums[1]
	else:
		tmp = nums[0] + nums[1]
		nums[0] = nums[1]
		nums[1] = tmp
	return fibb(n - 1)

print(fibb(5))


snt = "Hello there"
def revString(snt):
	if snt:
		return snt[-1] + revString(snt[:-1])
	else:
		return ""


nums = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
def bubble(arr):

	x, y = 0, 0
	while x <= len(arr) - 1:
		if arr[y] > arr[y + 1]:
			arr[y], arr[y + 1] = arr[y + 1], arr[y]

		if y + 2 > len(arr) - 1:
			x += 1
			y = 0
		else:
			y += 1


nums = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
def selection(arr):
	x, y = 0, 0
	current = 0
	while x <= len(arr) - 1:
		if arr[current] > arr[y]:
			current = y

		if y + 1 > len(arr) - 1:
			arr[x], arr[current] = arr[current], arr[x]
			x += 1
			y = x
		else:
			y += 1


nums = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
def insertion(arr):
	x, y = 0, 1
	while x <= len(arr) - 2:
		for i in range(x):
			if arr[y] > arr[i] and arr[y] < arr[i + 1]:
				arr.insert(i + 1, arr.pop(y))
			elif arr[y] < arr[i]:
				arr.insert(i, arr.pop(y))

		if y + 1 > len(arr) - 1:
			x += 1
			y = x + 1
		else:
			y += 1


nums = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
def mergeSort(arr):
	print(len(arr))
	if len(arr) > 2:
		splitIndex = int((len(arr) - 1) / 2)
		left = arr[splitIndex:]
		right = arr[:splitIndex]
	elif len(arr) == 2:
		return merge([arr[0]], mergeSort([arr[1]]))
	else:
		return arr
	
	return merge(mergeSort(left), mergeSort(right))

def merge(left, right):
	left.append(None)
	right.append(None)

	x, y = 0, 0
	new = []
	while True:
		if left[x] != None and right[y] != None:
			if left[x] > right[y]:
				new.append(right[y])
				y += 1
			else:
				new.append(left[x])
				x += 1
		else:
			if left[x] != None:
				new.append(left[x])
				x += 1
			elif right[y] != None:
				new.append(right[y])
				y += 1

		if left[x] == None and right[y] == None:
			break
	return new



