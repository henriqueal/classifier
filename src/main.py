import k_nn
import k_fold

normalization = true
k_of_kfold = 3
k_of_knn = 3
filename = "../input/dados.txt"

#Ler do usuario
#normalization = read()
#k_of_kfold = read()
#k_of_knn = read()
#filename = read()

#data = open(filename)

k_fold(data, normalization, k_of_kfold, k_of_knn)
