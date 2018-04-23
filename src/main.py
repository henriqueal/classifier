import sys
from normalizer import *
from quality_measurer import *

normalization = "y"
k_of_kfold = 3
k_of_knn = 3
filename = "dados.txt"

#Ler do usuario
#normalization = input("Deseja utilizar o z-score? (y/n)")

if(normalization == "y"):
    normalization = True
else:
    normalization = False 
	
#k_of_kfold = input("Por favor informe o numero de particoes do k-fold:")
#k_of_knn = input("Por favor informe o numero de vizinhos do k-NN:")
#filename = input("Por favor informe o nome do arquivo de dados:")
normalization = False

line_count = 0
data = []
numberSamples = 0
numberAttributes = 0


with open('../input/'+filename) as f:
    for line in f:
        if(line_count == 0):
            numberSamples = int(line.split(' ')[0])
            numberAttributes = int(line.split(' ')[1])
            line_count = line_count + 1
        else:
            matrix_line = line.split(' ')
            matrix_line[len(matrix_line)-1] = matrix_line[len(matrix_line)-1].split('\r\n')[0]
            array_data = []	
            for data_string in matrix_line:
                array_data.append(float(data_string))
            data.append(array_data)

if normalization:
	data = z_score(data)

array_answers = k_fold(data, k_of_kfold, k_of_knn,normalization)

total_correct = 0
total_wrong = 0
for i in range(len(array_answers)):
	total_correct = total_correct + array_answers[i][0]
	total_wrong = total_wrong + array_answers[i][1]
	
#print(array_answers)
print("Total correct: " + str(total_correct))
print("Total wrong: " + str(total_wrong))
print("Total: " + str(total_wrong+total_correct))
print("Pecentual: " + str((total_correct*100.0)/(total_wrong+total_correct)) + "%")