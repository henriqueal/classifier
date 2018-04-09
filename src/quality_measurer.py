#dic = {"test_size" : 10, "correct_answer" : 3, "wrong_answer" : 7}
def process(n, data, data_type):
	print ("process")



def k_fold(data, k_of_kfold, k_of_knn, normalization):

	dictlist = [dict() for x in range(len(k_of_kfold))]

	for i in range(len(k_of_kfold)):
		train_data = process(i,data, "train")
		test_data = process(i,data, "test")
		dictlist[i] = k_nn(train_data, test_data, k_of_knn, normalization)

	return dictlist
