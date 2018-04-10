def k_nn(train_data, test_data, k_of_knn, normalization):

	if(normalization):
		train_data = z_score(train_data)
		test_data = z_score(test_data)

	#mat : rows = test_data.len; cols = train_data.len 
	mat_of_distances = euclidean_distance(train_data, test_data)

   	mat_of_k_classes_nearest = k_nearest_classes(mat_of_distances, k)

	pair_classified = get_most_recurrence_class(mat_of_k_classes_nearest)
   	
	dict_of_answer = judge_answer(pair_classified) 

	return dict_of_answer
