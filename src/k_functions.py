def judge_answer(pair_classified, test_data):
	amount_data = len(test_data)
	
	correct_answer = 0
	wrong_answer = 0
	for i in range(0, amount_data):
		answer = [0,0]
		if (pair_classified[i] == test_data[i][len(test_data[0])-1]):
			correct_answer = correct_answer + 1
		else:
			wrong_answer = wrong_answer + 1
		answer[0] = correct_answer
		answer[1] = wrong_answer
	
	return answer

	
def exists_in_array(array, number):
	size = len(array)
	
	for i in range(0,size):
		if array[i] == number:
			return True
	return False
	
def k_min_array(array,k):
	novo_array = list(array)
	size = len(novo_array)
	results = []
	
	for j in range(0, k):
		min = novo_array[0]
		iteration_min = 0
		for i in range(0, size):
			if (novo_array[i] < min):
				min = novo_array[i]
				iteration_min = i
		novo_array[iteration_min] = 999999
		results.append(iteration_min)
	return results
	
	
# Esta funcao retorna as k classes mais proximas. É necessario passar como parametro a matriz
# de treinamento, em que a ultima coluna é a classe de cada dado
def k_nearest_classes(array_of_distances, k, mat_treinados):
	
	classes = get_classes(mat_treinados)
	##print("array_of_distances")
	##print(array_of_distances)
	
	##print("mat_treinados")
	##print(mat_treinados)
	
	k_nearest_classes = k_min_array(array_of_distances,k)

	##print("k_nearest_data")
	##print(k_nearest_classes)
	
	# substitui a matriz de dados mais proximos, pelas suas respectivas classes
	#for i in range(0, numberPoints):
	for j in range(0, k):
		k_nearest_classes[j] = classes[k_nearest_classes[j]]

		
	#print("k_nearest_classes")
	#print(k_nearest_classes)
	
		
	return k_nearest_classes
		
		
# funcao para somar 1 no numero definido na lista de indices
def sum_one_index_list(index_list, number):
	size = len(index_list)
	
	for i in range(0,size):
		if index_list[i][0] == number:
			index_list[i][1] = index_list[i][1] + 1
		
		
# retorna qual o indice em que o numero está		
def index_on_index_list(index_list, number):
	size = len(index_list)
	
	for i in range(0, size):
		if index_list[i][0] == number:
			return i
	return -1
		
# pega a maior recorrencia em um array. Se 2 tiverem a mesma quantia, retorna -1
def get_most_recurrence_in_array(array):
	size = len(array)
	
	index_list_amount = []
	
	for i in range(0,size):
		if (index_on_index_list(index_list_amount, array[i]) == -1):
			index_list_amount.append([array[i],1])
		else:
			index_list_amount[index_on_index_list(index_list_amount,array[i])][1] = index_list_amount[index_on_index_list(index_list_amount,array[i])][1] + 1
		
	size_index_list = len(index_list_amount)
	max = index_list_amount[0][1]
	higher = index_list_amount[0][0]
	max_index = 0
	for i in range(0,size_index_list):
		if index_list_amount[i][1] > max:
			max = index_list_amount[i][1]
			max_index = i
			#higher = index_list_amount[i][0]

	count = 0
	for i in range(0,size_index_list):
		if index_list_amount[i][1] == max:
			count = count + 1
			
	if (count == 1):
		return index_list_amount[max_index][0]
		
	# possui dois ou mais valores maximos com a mesma quantidade
	return -1

# retorna um vetor: o indice do vetor é o dado, e o valor no indice é a classe do dado
def get_classes(training_matrix):
	amount_lines = len(training_matrix)
	classes = []
	
	for i in range(0,amount_lines):
		classes.append(training_matrix[i][len(training_matrix[0])-1])
	
	return classes
	
# Retorna a classe que possui maior recorrencia
def get_most_recurrence_class(array_of_distances, k, training_matrix):
	k_classes = k_nearest_classes(array_of_distances, k, training_matrix)
	
	##print("k_classes antes:")
	##print(k_classes)
	
	while(get_most_recurrence_in_array(k_classes) == -1 and k > 0):
		##print("[[criterio de desempate = k-1]]")
		k = k-1
		k_classes = k_nearest_classes(array_of_distances, k, training_matrix)
	
	
	##print("k_classes depois:")
	##print(k_classes)
	
	return get_most_recurrence_in_array(k_classes)
