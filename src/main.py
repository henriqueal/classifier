import k_nn
import k_fold

normalization = true
k_of_kfold = 3
k_of_knn = 3
filename = "../input/dados.txt"

#Ler do usuario
normalization = raw_input("Deseja utilizar o z-score? (y/n)")

if(normalization == "y"):
    normalization = True
else:
    normalization = False

k_of_kfold = raw_input("Por favor informe o numero de particoes do k-fold:")
k_of_knn = raw_input("Por favor informe o numero de vizinhos do k-NN:")
filename = raw_input("Por favor informe o nome do arquivo de dados:")

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
            data.append(matrix_line)
        print(line)

print(data)

k_fold(data, normalization, k_of_kfold, k_of_knn)
