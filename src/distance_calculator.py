import math

def euclidean_distance(train_data, test_data):
	numberColumns = len(train_data[0]) # Calculando o numero de atributos da amostra
	result = []
	aux = []
	sum = 0.0
	position_train = 0
	position_test = 0
	position_column = 0

	while(position_test < len(test_data)):
		while(position_train < len(train_data)):
			while(position_column < numberColumns-1):
				sum = sum + (train_data[position_train][position_column] - test_data[position_test][position_column])**2
				position_column = position_column + 1
			aux.append(math.sqrt(sum))
			sum = 0.0
			position_train = position_train + 1
			position_column = 0

		result.append(aux)
		aux = []
		position_test = position_test + 1
		position_train = 0

	return result
