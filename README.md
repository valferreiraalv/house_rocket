# 1.0 House Rocket

O conjunto de dados em questão refere-se à plataforma de negócios digitais House Rocket que compra imóveis em boas localizações a preços baixos e vendem com valores altos.
E este conjunto de dados contém preços de venda de casas para King County, que inclui Seattle. Inclui casas vendidas entre maio de 2014 e maio de 2015.

# 2.0 Etapas 

- [aula 01_python.py](https://github.com/valferreiraalv/house_rocket/blob/main/notebooks/aula01_python.py)
- [aula 02_python.py](https://github.com/valferreiraalv/house_rocket/blob/main/notebooks/aula02_python.py)
- [aula 03_python.ipynb](https://github.com/valferreiraalv/house_rocket/blob/main/notebooks/aula03_python.ipynb)
- [aula 04_python.ipynb](https://github.com/valferreiraalv/house_rocket/blob/main/notebooks/aula04_python.ipynb)
- [aula 05_python.ipynb](https://github.com/valferreiraalv/house_rocket/blob/main/notebooks/aula05_python.ipynb)
- [aula 06_python.py](https://github.com/valferreiraalv/house_rocket/blob/main/notebooks/aula06_python.py)
- [aula 07_python.py](https://github.com/valferreiraalv/house_rocket/blob/main/notebooks/aula07_python.py)

# 3.0 Dicionário de Dados 

- id: ID único para cada casa vendida
- date: Data da venda da casa
- price: Preço de cada casa vendida
- bedrooms: Número de quartos
- bathrooms: Número de banheiros, onde 0,5 corresponde a um quarto com banheiro, mas sem chuveiro
- sqft_living: Metragem quadrada do espaço interior dos apartamentos
- sqft_lot: Metragem quadrada do espaço terrestre
- floors: Número de andares
- waterfront: - Uma variável fictícia para saber se o apartamento tinha vista para a beira-mar ou não
- view: Um índice de 0 a 4 de quão boa era a vista da propriedade
- condition: - Um índice de 1 a 5 sobre o estado do apartamento,
- grade: Um índice de 1 a 13, onde 1-3 fica aquém da construção e design do edifício, 7 tem um nível médio de 1. nível de construção e design e 11-13 tem um nível de construção e design de alta qualidade.
- sqft_above: A metragem quadrada do espaço habitacional interno que está acima do nível do solo
- sqft_basement: A metragem quadrada do espaço habitacional interno que está abaixo do nível do solo
- yr_built: O ano em que a casa foi construída inicialmente
- yr_renovated: O ano da última renovação da casa
- zipcode: Em qual CEP se encontra a casa
- lat: Latitude
- long: Longitude
- sqft_living15: A metragem quadrada do espaço interno de habitação para os 15 vizinhos mais próximos
- sqft_lot15: A metragem quadrada dos lotes de terreno dos 15 vizinhos mais próximos

# 4.0 Resolução 

O conteúdo deste curso contemplou a aplicação da linguagem python, extração, manipulação e transformação de dados, estruturas de controle, funções e organização de códigos além de visualização de dados para responder questões de negócios, sendo elaborada uma página por meio da biblioteca streamlit. A página foi disponibilizada com o deploy no Heroku e pode ser acessado por meio do link: https://analysis-house-stream.herokuapp.com/

<p align="center">
  <img width="460" height="300" src="src/assets/to_readme/app_dashboard_Streamlit.gif">
 </p>
