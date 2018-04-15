
def exists_in_array(array, number):
	size = len(array)
	
	for i in range(0,size):
		if array[i] == number:
			return True
	return False
	
def k_max_array(array,k):
	size = len(array)
	results = []
	k_array = []
	
	for j in range(0, k):
		max = array[0]
		iteration_max = 0
		for i in range(0, size):
			if (array[i] > max and (exists_in_array(results,i) == False)):
				max = array[i]
				iteration_max = i

		results.append(iteration_max)
	
	return results
	
def k_nearest_classes(mat_of_distances, k):
	
	numberPoints = len(mat_of_distances[0])
	mat_result = []
	
	for point in range(0,numberPoints):
		mat_result.append(k_max_array(mat_of_distances[point],k))

	return mat_result

def show_array(array):
	size = len(array)
	
	for i in range(0,size):
		print(array[i])

def show_matrix(matrix):
	amount_columns = len(matrix[0])
	amount_lines = len(matrix)
	
	for i in range(0,amount_lines):
		for j in range(0, amount_columns):
			print(matrix[i][j], end='')
			print(" ", end='')
		print ('')
		
		
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
		
		
def get_most_recurrence(array):
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
	for i in range(0,size_index_list):
		if index_list_amount[i][1] > max:
			max = index_list_amount[i][1]
			higher = index_list_amount[i][0]

	return higher

	
def get_most_recurrence_class(matrix):
	amount_lines = len(matrix)
	result = []
	
	for i in range(0,amount_lines):
		result.append(get_most_recurrence(matrix[i]))
	
	return result

#index_list = []
#index_list.append([7,2])
#index_list.append([19,1])
#index_list.append([10,1])
#index_list.append([20,1])

#print(index_list[0][1])

#print(index_on_index_list(index_list,10))


#array = [1,2,2,2,2,2,2,2,2,9,9,9,9,9,9,9,9,9,20,20,20,20,20,20,20,20,3,4,5]
#array = [1,2,3,4]
#print(get_most_recurrence(array))

	
	
#array1 = [0,2,3,4,7]
#array2 = [2,0,3,1,5]
#array3 = [3,3,0,2,6]
#array4 = [4,1,2,0,8]
#array5 = [7,5,6,8,0]
#matrix_distances = []
#matrix_distances.append(array1)
#matrix_distances.append(array2)
#matrix_distances.append(array3)
#matrix_distances.append(array4)
#matrix_distances.append(array5)

#show_matrix(matrix_distances)

#k = 3
#k_classes = k_nearest_classes(matrix_distances, k)

#show_matrix(k_classes)

#most_recurrence_class = get_most_recurrence_class(k_classes)

#print()
#print()
#print()
#show_array(most_recurrence_class)