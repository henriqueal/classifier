def mean(data):
	print("input: matriz de dados")
	print("output: deve retornar um vetor com as medias de cada coluna da matriz")
	return 1

def standard_deviation(data):
	print("input: matriz de dados")
	print("output: deve retornar um vetor com os desvios padroes de cada coluna da matriz")
	return 1

def z_score(data):
	mean = mean(data)
	dev = standard_deviation(data)
	
	for i range(len(data)):
		for j in range(len(data[i])):
			data[i][j] = (data[i][j] - mean[j])/dev[j]
	return data

z_score(range(2))
