import math as m

def quick_sort(a):
	if len(a) <= 1:
		return a
	pivot = (int)(len(a) / 2)
	temp = a[pivot]
	a[pivot] = a[-1]
	a[-1] = temp
	last_index = -1
	for i in range(len(a)):
		if a[i] > a[-1]:
			if last_index == -1:
				last_index = i
			for j in range(last_index, len(a) - 1):
				if a[j] <= a[-1]:
					temp = a[i]
					a[i] = a[j]
					a[j] = temp
					last_index = i + 1
					break
	if last_index != -1:
		temp = a[-1]
		a[-1] = a[last_index]
		a[last_index] = temp
		result = quick_sort(a[:last_index])
		result.append(a[last_index])
		result.extend(quick_sort(a[last_index + 1:]))
		return result

	return a

a = [9, 7, 6, 5, 3, 2, 1]
b = [2, 7, 8, 4, 1, 11]

print(quick_sort(b))
