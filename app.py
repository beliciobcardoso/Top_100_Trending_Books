import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title='Book Review Analysis', layout='wide')

df_reviews = pd.read_csv('datasets/customer_reviews.csv')
df_top100_books = pd.read_csv('datasets/Top_100_Trending_Books.csv')
# print(df_top100_books.index)
# print(df_top100_books.head())
# print(df_top100_books.columns)
# Index(['Rank', 'book title', 'book price', 'rating', 'author',
#        'year of publication', 'genre', 'url'],
#       dtype='object')

price_max = df_top100_books['book price'].max()
price_min = df_top100_books['book price'].min()
# print(price_max, price_min)


faixa_price = st.sidebar.slider(
    'Select a range of values',
    price_min, price_max, (10.0, 30.0))
# print(faixa_price[0])

# Criar um slider para selecionar o preço min e max
max_price = st.sidebar.slider(
    "Price Range", faixa_price[0], faixa_price[1], faixa_price[1])
# print(max_price)

# Filtrar a tabela de livros com base no preço
df_books = df_top100_books[df_top100_books['book price'] <= max_price]

# Exibir a tabela de livros
df_books

# fig01 = px.bar(df_books, x='book title', y='rating', color='author', title='Top 100 Books')
fig01 = px.bar(df_books["year of publication"].value_counts())

fig02 = px.histogram(df_books["book price"], title='Price Distribution', nbins=20, labels={
                     'value': 'Price', 'count': 'Frequency'})

clo01, clo02 = st.columns(2)
clo01.plotly_chart(fig01)
clo02.plotly_chart(fig02)
