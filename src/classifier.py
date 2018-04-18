def k_nn(train_data, test_data, k_of_knn, normalization):

	if(normalization):
		train_data = z_score(train_data)
		test_data = z_score(test_data)

	#mat : rows = test_data.len; cols = train_data.len 
	mat_of_distances = euclidean_distance(train_data, test_data)
	amount_test = len(test_data)
	
	pair_classified = []
	for iteration in range(0, amount_test):
		pair_classified.append(get_most_recurrence_class(iteration, mat_of_distances[iteration], k, training_matrix))
   	
	dict_of_answer = judge_answer(pair_classified) 

	return dict_of_answer
