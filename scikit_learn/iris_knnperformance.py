# Por fim, precisamos determinar o percentual de acerto dos meus dados
# Também precisamos separar nossos dados em dois grupos.
# Esses dois grupos são necessários pois nós precisamos ter certeza de que quando o computador for fazer a previsão, ele possa fazer a previsão com dados que ainda não teve acesso.

from sklearn.datasets import load_iris
iris = load_iris()

x = iris.data
y = iris.target

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)

knn.fit(x,y)

print(knn.predict([[5.1,3.5,1.4,0.2]]))

# #Grupo 1: Treinamento da máquina
from sklearn.model_selection import train_test_split #Separa os dados em dois grupos. Facilita a separação de dados
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25) # precisamos de 2 variáveis X e duas variáveis Y. Uma vai ser para treinar a máquina e o restante para teste

#Grupo 2: Avaliação de performance
knn.fit(x_train, y_train)
print(x_test)
print(y_test)

previsoes = knn.predict(x_test)

#comparar as previsões com as respostas
from sklearn import metrics
acertos = metrics.accuracy_score(y_test, previsoes)
print(acertos)

print(y_test)
print(previsoes)