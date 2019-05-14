def counting_sort(aux, k):
	#kount = [0] * 10 #base 10
	kindex = {0:[], 1 : [], 2 : [], 3: [], 4 : [], 5:[],
			6:[], 7:[], 8:[], 9:[]} #base 10

	for j in range(0,len(aux)):
		#print(j, type(j))
		kindex[int(aux[j][k])].append(j)

	#print("aux: ", aux)
	#print(kount)
	#print(kindex)
	newa = []

	for keys in kindex:
		#print(keys)
		for item in kindex[keys]:
			newa.append(aux[item])

	#print("new",newa)
	return newa



def radix_sort(a):
	m = len(str(max(a)))

	aux = []
	for i in a:
		temp = str(i)
		while len(temp) < m:
			temp = "0" + temp
		aux.append(temp)

	for i in range(0, m):
		aux = counting_sort(aux, m - 1 - i)

	
	return list(map(int, aux))


a = [52, 3, 312, 1, 60, 4, 111]
print(radix_sort(a))