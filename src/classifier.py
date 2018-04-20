from k_functions import *
from normalizer import *

def k_nn(train_data, test_data, k_of_knn, normalization):

	#if(normalization):
	#	train_data = z_score(train_data)
	#	test_data = z_score(test_data)

	
	
	#mat : rows = test_data.len; cols = train_data.len 
	mat_of_distances = euclidean_distance(train_data, test_data)
	amount_test = len(test_data)
	
	# Iterando dado a dado
	# o pair_classified é somente com as classes. Os índices são os indices dos dados
	pair_classified = []
	for iteration in range(0, amount_test):
		pair_classified.append(get_most_recurrence_class(mat_of_distances[iteration], k_of_knn, train_data))
   	
	# Nessa funcao judge_answer, a matriz test_data precisa conter as classes na posicao [4]
	# ela retorna um vetor: 1a posicao: qtd_correct_answer, 2a posicao: qtd_wrong_answer
	array_of_answer = judge_answer(pair_classified, test_data)
	
	# falta implementar essa array_to_dic
	#dict_of_answer = array_to_dic(array_of_answer)

	return array_of_answer