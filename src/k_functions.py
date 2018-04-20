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
	print("array_of_distances")
	print(array_of_distances)
	
	print("mat_treinados")
	print(mat_treinados)
	
	k_nearest_classes = k_min_array(array_of_distances,k)

	print("k_nearest_data")
	print(k_nearest_classes)
	
	# substitui a matriz de dados mais proximos, pelas suas respectivas classes
	#for i in range(0, numberPoints):
	for j in range(0, k):
		k_nearest_classes[j] = classes[k_nearest_classes[j]]

		
	print("k_nearest_classes")
	print(k_nearest_classes)
	
		
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
	
	print("k_classes antes:")
	print(k_classes)
	
	while(get_most_recurrence_in_array(k_classes) == -1 and k > 0):
		print("[[criterio de desempate = k-1]]")
		k = k-1
		k_classes = k_nearest_classes(array_of_distances, k, training_matrix)
	
	
	print("k_classes depois:")
	print(k_classes)
	
	return get_most_recurrence_in_array(k_classes)

array1 = [9,2,3,4,1]
array2 = [3,3,3,1,1]
array3 = [3,3,9,2,2]
array4 = [4,1,2,9,2]
array5 = [7,5,6,8,3]
training_matrix = []
training_matrix.append(array1)
training_matrix.append(array2)
training_matrix.append(array3)
training_matrix.append(array4)
training_matrix.append(array5)

	
	
array1 = [9,2,3,4,7]
array2 = [3,3,3,1,3]
array3 = [3,3,9,2,6]
array4 = [4,1,2,9,8]
array5 = [7,5,6,8,9]
matrix_distances = []
matrix_distances.append(array1)
matrix_distances.append(array2)
matrix_distances.append(array3)
matrix_distances.append(array4)
matrix_distances.append(array5)

print("distance_matrix")
print(matrix_distances)

k = 4

for i in range(0, len(matrix_distances)):
	#print("---------------------")
	print(get_most_recurrence_class(matrix_distances[i], k, training_matrix))
	print("---------------------")

#show_array(most_recurrence_class)


	
#vetor = [1,2,3,4,5]

#teste = []
#a_teste1 = [0,0,0,0,1]
#a_teste2 = [0,0,0,0,1]
#a_teste3 = [0,0,0,0,2]
#a_teste4 = [0,0,0,0,4]
#a_teste5 = [0,0,0,0,5]
#teste.append(a_teste1)
#teste.append(a_teste2)
#teste.append(a_teste3)
#teste.append(a_teste4)
#teste.append(a_teste5)

#print("judge:")
#print(judge_answer(vetor,teste))
	
	