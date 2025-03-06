import pandas as pd
df = pd.read_csv('heart_disease_risk_dataset_earlymed.csv', encoding = 'latin-1')
print(df)
x = df.drop(columns=['Heart_Risk'])
y = df['Heart_Risk']

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=5)

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size= 0.20)

knn.fit(x_train, y_train)

previsao = knn.predict(x_test)

from sklearn import metrics
acertos = metrics.accuracy_score(y_test, previsao)

print(acertos)