from k_functions import *
from normalizer import *

def k_nn(train_data, test_data, k_of_knn, normalization):

	
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
	
	return array_of_answer