#Importação do dataset Iris que já vem incluso no Sklearn como exemplo
from sklearn.datasets import load_iris
iris = load_iris() # Não esquecer de colocar () quando for carregar o dataset

print(iris.data) # é Um array Numpy. Essas Arrays são mais eficientes, ocupam menos memoria e são mais rápidas
print(iris.target) #Target são os resultados.
print(iris.target_names) #Mostra o nome dos resultados. O codigo anterior apenas mostra o número referente a resposta

# Para trabalhar com machine learning sempre teremos dois arrays separados. Um array é para as observações e outro serão os resultados dessas observações
# O número de observações deve ser o mesmo dos resultados. Para isso podemos usar o comando shape para verificar.

print(iris.data.shape)
print(iris.target.shape)