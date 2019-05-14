def bubbleSort(a):
	swap =  True
	n = len(a)
	i = -1

	while(swap):
		i += 1
		swap = False
		for j in range(0, n - i - 1):
			if a[j+1] < a[j]:
				a[j], a[j+1] = a[j+1], a[j]
				swap = True
	return a



a = [52, 3, 312, 1, 60, 4, 111]
print(bubbleSort(a))