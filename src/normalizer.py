def mean(data):
	print("deve retornar a media dos dados")
	return 1

def standard_deviation(data):
	print("deve retornar o desvio padrao dos dados")
	return 1

def z_score(data):
	mean = mean(data)
	dev = standard_deviation(data)
	
	for i range(len(data)):
		data[i] = (data[i] - mean)/dev
	return data

z_score(range(2))
