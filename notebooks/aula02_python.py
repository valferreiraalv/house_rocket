# carregando dados

import pandas as pd
import statistics
import math
from scipy import stats
import numpy
from collections import Counter
data = pd.read_csv('datasets/kc_house_data.csv')

# 1. Crie uma nova coluna chamada: “house_age”
# - Se o valor da coluna “date” for maior que 2014-01-01 =>‘new_house’
# - Se o valor da coluna “date” for menor que 2014-01-01 => ‘old_house’

data['house_age'] = 'feature'
data.loc[data['date'] > '2014-01-01', 'house_age'] = 'new_house'
data.loc[data['date'] < '2014-01-01', 'house_age'] = 'old_house'
print(data.head())

# 2. Crie uma nova coluna chamada: “dormitory_type”
# - Se o valor da coluna “bedrooms” for igual à 1 => ‘studio’
# - Se o valor da coluna “bedrooms” for igual a 2 => ‘apartament’
# - Se o valor da coluna “bedrooms” for maior que 2 => ‘house’

data['dormitory_type'] = 'feature'
data.loc[data['bedrooms'] == 1, 'dormitory_type']= 'studio'
data.loc[data['bedrooms'] == 2, 'dormitory_type']= 'apartament'
data.loc[data['bedrooms'] > 2, 'dormitory_type']= 'house'
print(data.head())

# 3. Crie uma nova coluna chamada: “condition_type”
# - Se o valor da coluna “condition” for menor ou igual à 2 => ‘bad’
# - Se o valor da coluna “condition” for igual à 3 ou 4 => ‘regular’
# - Se o valor da coluna “condition” for igual à 5 => ‘good’

data['condition_type'] = 'aspect'
data.loc[data['condition'] <= 2, 'condition_type']= 'bad'
data.loc[data['condition'] == 3 ^ 4, 'condition_type']= 'regular'
data.loc[data['condition'] == 5, 'condition_type']= 'good'
print(data.head())

# 4. Modifique o TIPO a Coluna “condition” para STRING
data['condition']=data['condition'].astype(str)
print(data.dtypes)

# 5. Delete as colunas: “sqft_living15” e “sqft_lot15”
print(data.columns)
cols= ['sqft_living15','sqft_lot15']
data=data.drop(cols, axis=1)
print(data.columns)

# 6. Modifique o TIPO a Coluna “yr_build” para DATE
#data['yr_build']= pd.to_datetime(data['yr_build'])

# 7. Modifique o TIPO a Coluna “yr_renovated” para DATE


# 8. Qual a data mais antiga de construção de um imóvel?
print(data['yr_built'].min())

# 9. Qual a data mais antiga de renovação de um imóvel?
print(data['yr_renovated'].min())

# 10. Quantos imóveis tem 2 andares?
#print(data[sum.data['floors']==2])

# 11. Quantos imóveis estão com a condição igual a “regular” ?
#print(data['regular'].value_counts())
#print(data[df.groupby('condition_type').count()])

# 12. Quantos imóveis estão com a condição igual a “bad”e possuem “vista para água” ?

# 13. Quantos imóveis estão com a condição igual a “good” e são “new_house”?

# 14. Qual o valor do imóvel mais caro do tipo “studio” ?

# 15. Quantos imóveis do tipo “apartment” foram reformados em 2015 ?

# 16. Qual o maior número de quartos que um imóveis do tipo “house” possui ?

# 17. Quantos imóveis “new_house” foram reformados no ano de 2014?

# 18. Selecione as colunas: “id”, “date”, “price”, “floors”, “zipcode” pelo método:

# 18.1. Direto pelo nome das colunas.

# 18.2. Pelos Índices.

# 18.3. Pelos Índices das linhas e o nome das colunas

# 18.4. Índices Booleanos

# 19. Salve um arquivo .csv com somente as colunas do item 10 ao 17.

# 20. Modifique a cor dos pontos no mapa de “pink” para “verde-escuro”
