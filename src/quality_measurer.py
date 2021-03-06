import math
import random
import time
from classifier import *

def searchByClass(data,targetClass):
	# search a sample that has a specific class and return the position
	while(1):
		position_try = random.randint(0,len(data)-1)
		if(data[position_try][len(data[position_try])-1] == targetClass):
			return position_try

def distinctClasses(data):
	# return an array of all the distinct classes in the data
	result = []
	for sample in data:
		if((sample[len(sample)-1] in result) == False):
			result.append(sample[len(sample)-1])
	return result

def process(k_of_kfold, i, data, data_type, method, lastTestGroups):
	data_size = len(data)
	data_group_size = int(math.ceil(data_size / float(k_of_kfold)))

	if(method == "standard"):

		line_count = 0
		line_count_aux = 0
		group_count = 0

		result_matrix = []

		for data_line in data:

			if((group_count == i and data_type == "test") or (group_count != i and data_type == "train")):
				result_matrix.append(data_line)
			if(line_count_aux == data_group_size-1):
				line_count_aux = 0
				group_count = group_count + 1
			else:
				line_count_aux = line_count_aux + 1
			line_count = line_count + 1
		return result_matrix

	if(method == "random"):
		line_count = 0
		group_count = 0
		result_matrix = []
		if(data_type == "train"):
			while(line_count < (data_size - data_group_size)):
				random_next = random.randint(0,(len(data)-1))
				result_matrix.append(data[random_next])
				del data[random_next]
				line_count = line_count + 1

		if(data_type == "test"):
			while(line_count < (data_group_size)):
				random_next = random.randint(0,(len(data)-1))
				if((data[random_next] in lastTestGroups) == False):
					result_matrix.append(data[random_next])
					del data[random_next]
				line_count = line_count + 1
		return result_matrix

	if(method == "serialize"):
		line_count = 0
		group_count = 0
		result_matrix = []
		classes = distinctClasses(data)

		if(data_type == "train"):
			pos = 0
			for i in range(0,(data_size - data_group_size)):
				chosenOne = searchByClass(data,classes[pos])
				result_matrix.append(data[chosenOne])
				print("Tamanho do resultado de treinamento: "+str(len(result_matrix)))
				print("Tamanho dos dados (clone da iteracao atual): "+str(len(data)))

				del data[chosenOne]
				pos = (pos + 1) % len(classes)


		if(data_type == "test"):
			pos = 0
			for i in range(0,(data_group_size)):
				chosenOne = 0
				if(len(lastTestGroups)>=1):
					for group in lastTestGroups:
						while((data[chosenOne] in group)==True):
							chosenOne = searchByClass(data,classes[pos])
				else:
					chosenOne = searchByClass(data,classes[pos])
				result_matrix.append(data[chosenOne])
				print("Tamanho do resultado de teste: "+str(len(result_matrix)))
				print("Tamanho dos dados (clone da iteracao atual): "+str(len(data)))

				del data[chosenOne]
				pos = (pos + 1) % len(classes)

		return result_matrix

def k_fold(data, k_of_kfold, k_of_knn, normalization):

	matrix_answers = []
	testSamples =[]
	processType = "random"
	for i in range(k_of_kfold):
		copia = list(data)
		test_data = process(k_of_kfold, i, copia , "test",processType, testSamples)
		testSamples.append(test_data)
		train_data = process(k_of_kfold, i, copia, "train", processType, testSamples)
		matrix_answers.append(k_nn(train_data, test_data, k_of_knn, normalization))

	return matrix_answers