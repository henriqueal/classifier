#dic = {"test_size" : 10, "correct_answer" : 3, "wrong_answer" : 7}
import math
from classifier import *

def process(k_of_kfold, i, data, data_type):
	#print("process")
	#print(data)
	#print(k_of_kfold)
	#print(i)
	#print(data_type)
	
	data_size = len(data)
	#print("DATASIZE "+str(data_size))
	data_group_size = int(math.ceil(data_size / float(k_of_kfold)))

	line_count = 0
	line_count_aux = 0
	group_count = 0

	result_matrix = []

	#print("Comecando iteracoes:")

	for data_line in data:

		#print("linha:"+str(data_line))
		#print("num linha:"+str(line_count))
		#print("num linha aux:"+str(line_count_aux))
		#print("tam do grupo:"+str(data_group_size))
		#print("num grupo:"+str(group_count))

		
		if((group_count == i and data_type == "test") or (group_count != i and data_type == "train")):
			result_matrix.append(data_line)		
		if(line_count_aux == data_group_size-1):
			line_count_aux = 0
			group_count = group_count + 1	
		else:		
			line_count_aux = line_count_aux + 1
		line_count = line_count + 1
	return result_matrix
				

def k_fold(data, k_of_kfold, k_of_knn, normalization):

	#dictlist = [dict() for x in range(len(k_of_kfold))]
	matrix_answers = []
	
	
	for i in range(k_of_kfold):
		
		train_data = process(k_of_kfold, i, data, "train")
		test_data = process(k_of_kfold, i, data, "test")
		#print("--------------")
		#print("i")
		#print(i)
		#print("test_data")
		#print(test_data)
		#print("train_data")
		#print(train_data)
		#print("--------------")
		#print(k_nn(train_data, test_data, k_of_knn, normalization))
		matrix_answers.append(k_nn(train_data, test_data, k_of_knn, normalization))

	return matrix_answers
