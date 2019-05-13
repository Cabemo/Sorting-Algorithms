import math as m

def heap_sort(a):
	ordered = []
	a.insert(0, -1)
	for i in range((int)(m.floor(len(a) - 1) / 2), 0, -1):
		heapify(a, i)
	print(a)
	while len(a) > 1:
		ordered.append(a[1])
		swap(a, 1, len(a) - 1)
		a.pop()
		if len(a) != 2:
			heapify(a, 1)
	return ordered

def heapify(a, i):
	n = len(a)
	if n == 3:
		if a[i] < a[2*i]:
			swap(a, i, 2*i)
			return True
		return False
	if i > m.floor(n/2 - 1):
		return False
	else:
		largest = i
		if a[2*i] > a[i]:
			largest = 2*i
		if a[2*i + 1] > a[largest]:
			largest = 2*i + 1
		if i != largest:
			swap(a, i, largest)
			heapify(a, largest)	
			return True
	return False
def swap(a, i, j):
	temp = a[i]
	a[i] = a[j]
	a[j] = temp
a = [4, 1, 6, 8, 9, 5, 2]
print(a)
print(heap_sort(a))