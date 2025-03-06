#Usado comumente para combinações binárias (permitem apenas dois tipos de classificação
from sklearn.datasets import load_iris
iris = load_iris()

x= iris.data
y = iris.target

print(iris.data)
#Grupo 1: Treinamento da máquina
from sklearn.model_selection import train_test_split #Separa os dados em dois grupos. Facilita a separação de dados
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25) # precisamos de 2 variáveis X e duas variáveis Y. Uma vai ser para treinar a máquina e o restante para teste

from sklearn.linear_model import LogisticRegression

logreg = LogisticRegression()
logreg.fit(x_train,y_train)

previsoes_logreg = logreg.predict(x_test)

from sklearn import metrics
acertos_logreg = metrics.accuracy_score(y_test, previsoes_logreg)

print(acertos_logreg)