from distance_calculator import *
import math

def mean_of_data(data):
	column = 0
	line = 0
	result = []
	sum = 0

	while(column < len(data[0])):
		while(line < len(data)):
			sum = sum + data[line][column]
			line = line + 1
		result.append(sum/(len(data)))
		sum = 0
		line = 0
		column = column + 1

	return result

def standard_deviation(data,mean):
	column = 0
	line = 0
	sum = 0
	result = []

	while(column < len(data[0])):
		while(line < len(data)):
			sum = sum + ((data[line][column] - mean[column])**2)
			line = line + 1
		result.append(math.sqrt(sum/(len(data)-1)))
		column = column + 1
		line = 0
		sum = 0


	return result

def z_score(data):	
	mean = mean_of_data(data)
	dev = standard_deviation(data,mean)

	for i in range(len(data)):
		for j in range(len(data[i])):
			if(j < len(data[i]) - 1):
				data[i][j] = (data[i][j] - mean[j])/dev[j]
	return data
