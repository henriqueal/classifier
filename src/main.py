import sys
from normalizer import *
from quality_measurer import *

normalization = "n"
k_of_kfold = 3
k_of_knn = 3
filename = "dados_random.txt"

#Ler do usuario
<<<<<<< HEAD
#normalization = input("Deseja utilizar o z-score? (y/n)")
=======
normalization = raw_input("Deseja utilizar o z-score? (y/n)")
>>>>>>> Diego

if(normalization == "y"):
    normalization = True
else:
<<<<<<< HEAD
    normalization = False 
	
#k_of_kfold = input("Por favor informe o numero de particoes do k-fold:")
#k_of_knn = input("Por favor informe o numero de vizinhos do k-NN:")
#filename = input("Por favor informe o nome do arquivo de dados:")
=======
    normalization = False

k_of_kfold = raw_input("Por favor informe o numero de particoes do k-fold:")
k_of_knn = raw_input("Por favor informe o numero de vizinhos do k-NN:")
filename = raw_input("Por favor informe o nome do arquivo de dados:")
>>>>>>> Diego

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

#print("data:")
#print(data)
if normalization:
	data = z_score(data)

print(k_fold(data, k_of_kfold, k_of_knn,normalization))
