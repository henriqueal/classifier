import math

def euclidean_distance(train_data, test_data):
	print("Deve retornar a matriz de distancia entre o vetor de teste e o de treinamento");
	print("Quantidade de linhas: tamanho do vetor de teste");
	print("Quantidade de colunas: tamanho do vetor de treinamento");

	numberColumns = len(train_data[0]) # Calculando o numero de atributos da amostra
	result = []
	aux = []
	sum = 0.0
	position = 0
	position_test = 0
	position_column = 0

	while(position < len(train_data)):
		print("Position:"+str(position))
		while(position_test < len(test_data)):
			while(position_column < numberColumns):
				sum = sum + (train_data[position][position_column] - test_data[position_test][position_column])**2
				print("["+str(position)+"]["+str(position_column)+"]"+" ["+str(position_test)+"]["+str(position_column)+"]")
				position_column = position_column + 1
			print(math.sqrt(sum))
			aux.append(math.sqrt(sum))
			sum = 0.0
			position_test = position_test + 1
			position_column = 0

		result.append(aux)
		aux = []
		position = position + 1
		position_test = 0

	return result




#print(euclidean_distance([[0,1,3],[2,4,5],[6,7,10]], [[11,12,13],[20,21,23],[40,50,60]]))
