import pandas as pd
df = pd.read_csv('vagass.csv', encoding = 'latin-1')
termox = df.drop(columns=['Termo'])
termoy = df['Termo']


from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

termox_train, termox_test, termoy_train, termoy_test = train_test_split(termox,termoy, test_size=0.20)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(termox_train.values,termoy_train)


a = float(input('1 - O aluno sabe python? Sim[1] ou Não[0]: '))
b = float(input('2 - O aluno sabe Selenium? Sim[1] ou Não[0]: '))
c = float(input('3 - O aluno sabe Beautiful Soup? Sim[1] ou Não[0]: '))
d = float(input('4 - O aluno sabe Scikit Learn? Sim[1] ou Não[0]: ')) 
e = float(input('5 - O aluno sabe Numpy? Sim[1] ou Não[0]: '))
f = float(input('6 - O aluno sabe Pandas? Sim[1] ou Não[0]: '))
g = float(input('7 - O aluno sabe Linguagem r? Sim[1] ou Não[0]: '))
h = float(input('8 - O aluno sabe Banco de dados? Sim[1] ou Não[0]: '))
i = float(input('9 - O aluno sabe Deep Learning? Sim[1] ou Não[0]: '))
j = float(input('10 - O aluno sabe Machine Learning? Sim[1] ou Não[0]: '))
k = float(input('11 - O aluno sabe Data Science? Sim[1] ou Não[0]: '))
l = float(input('12 - O aluno sabe Sistemas Embarcados IoT? Sim[1] ou Não[0]: '))
m = float(input('13 - O aluno sabe IA Generativa? Sim[1] ou Não[0]: '))
n = float(input('14 - O aluno sabe CyberSecurity? Sim[1] ou Não[0]: '))


previsao = knn.predict([[a,b,c,d,e,f,g,h,i,j,k,l,m,n]])


print(f'O aluno tem experiencia de um aluno do {previsao} termo')

from sklearn import metrics
valores_performance = {}
z = 1

while z <= 25:
    knn = KNeighborsClassifier(n_neighbors=z)
    knn.fit(termox_train,termoy_train)
    previsoes = knn.predict(termox_test)
    acertos = metrics.accuracy_score(termoy_test,previsoes)
    valores_performance[z] = round(acertos, 4)
    z += 1

print(valores_performance)