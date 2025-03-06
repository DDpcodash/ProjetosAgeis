from sklearn.datasets import load_iris
iris = load_iris()

#Por convenção, adota-se como X as observações da minha amostra
x = iris.data
print(x)

#Por convenção, adota-se como Y o resultado das observações
y = iris.target
print(y)

#Pelo método do KNN, devemos primeiro importar a biblioteca do KNN
from sklearn.neighbors import KNeighborsClassifier

#Criar uma variável que puxe o comando do KNN, sendo que dentro dele deve-se determinar o valor de K
knn = KNeighborsClassifier(n_neighbors=1)

#Em seguida, precisamos treinar nosso computador. Ou seja, cruzar as observações com os resultados.
knn.fit(x,y) #knn.fit, agrupa 2 arrays numpys e cruzam as informações.

#Após a máquina ser treinada com as amostras, devemos verificar as previsões
species = knn.predict([[5.1,3.5,1.4,0.2]])
print(iris.target_names[species])