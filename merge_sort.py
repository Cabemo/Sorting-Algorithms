def merge(a, b):
	result = []
	while a and b:
		if a[0] <= b[0]:
			result.append(a[0])
			a.pop(0)
		else:
			result.append(b[0])
			b.pop(0)
	if a:
		result.extend(a)
	else:
		result.extend(b)
	return result

def merge_sort(a):
	if len(a) == 1:
		return a
	half = (int)(len(a) / 2)
	return merge(merge_sort(a[:half]), merge_sort(a[half:]))

a = [5, 3, 1, 6, 4]
print(merge_sort(a))