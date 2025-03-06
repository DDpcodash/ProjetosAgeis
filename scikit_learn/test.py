import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('500hits.csv', encoding = 'latin-1')

x = df.drop(columns=['PLAYER', 'HOF'])
y = df['HOF']

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=20)

x_test, x_train, y_test, y_train = train_test_split(x,y, test_size=0.20)

knn.fit(x_train,y_train)
previsao = knn.predict(x_test)

from sklearn import metrics

acerto = metrics.accuracy_score(y_test, previsao)

valores_performance = {}
k = 1

while k <= 25:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train,y_train)
    previsoes = knn.predict(x_test)
    acertos = metrics.accuracy_score(y_test,previsoes)
    valores_performance[k] = round(acertos, 4)
    k += 1

print(valores_performance)