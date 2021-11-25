# carregando dados

import pandas as pd
import statistics
import math
from scipy import stats
import numpy
from collections import Counter
data = pd.read_csv('datasets/kc_house_data.csv')

#1. Quantas casas estão disponíveis para compra? #R: Contar a quantidade de linhas do conjunto de dados
print(data.head())

#2. Quantos atributos as casas possuem? ( Tamanho, preço, m2, quartos, … )? #R: Contar a quantidade de colunas do conjunto de dados
print(data.shape)

#3. Quais são os atributos das casas? #R: Mostrar o nome das colunas do conjunto de dados
print(data.columns)

#4. Qual a casa mais cara ( casa com o maior valor de venda )?( casa de maior valor de venda )? #R: Ordenar o conjunto de dados pelo preço das casas
print(data[['id','price']].sort_values('price'))

#5. Qual a casa com o maior número de quartos? #R: Ordenar o conjunto de dados pelo número.
print(data[['id','bedrooms']].sort_values('bedrooms', ascending=False))

#6. Qual a soma total de quartos do conjunto de dados?

#7. Quantas casas possuem 2 banheiros?
print(data[data.bathrooms == 2])

#8. Qual o preço médio de todas as casas no conjunto de dados?
#print(data[['id','price']].statistics.meam('price'))

#9. Qual o preço médio de casas com 2 banheiros?

#10. Qual o preço mínimo entre as casas com 3 quartos?

#11. Quantas casas possuem mais de 300 metros quadrados na sala de estar?
print(data[data['sqft_living'] > 300][['sqft_living','id']])

#12. Quantas casas tem mais de 2 andares?
print(data[data['floors'] == 2][['floors','id']])

#13. Quantas casas tem vista para o mar?
print(data[['id','waterfront']].value_counts())

#14. Das casas com vista para o mar, quantas tem 3 quartos?
print(data[['id','waterfront','bedrooms']].value_counts('bedrooms')==3)

#15. Das casas com mais de 300 metros quadrados de sala de estar, quantas tem mais de 2 banheiros?

print(data[['id','sqft_living'] > 300].value_counts('bathrooms')==2)
