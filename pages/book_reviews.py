import pandas as pd
import streamlit as st

df_reviews = pd.read_csv('datasets/customer_reviews.csv')
df_top100_books = pd.read_csv('datasets/Top_100_Trending_Books.csv')

# Lista de livros únicos em uma lista[]
books = df_top100_books['book title'].unique()
# print(len(books))

book = st.sidebar.selectbox('Select a book', books)

# Filtrar a tabela de livros com base no titulo do livro
df_books = df_top100_books[df_top100_books['book title'] == book]
df_reviews_f = df_reviews[df_reviews['book name'] == book]

book_title = df_books['book title'].values[0]
book_genre = df_books['genre'].values[0]
book_price = f"$ {df_books['book price'].values[0]}"
book_rating = df_books['rating'].values[0]
book_year = df_books['year of publication'].values[0]

st.title(book_title)
st.subheader(book_genre)
col01, col02, col03 = st.columns(3)
col01.metric('Price', book_price)
col02.metric('Rating', book_rating)
col03.metric('Year', book_year)

st.divider()

for row in df_reviews_f.values:
    massge = st.chat_message(f"{row[4]}")
    massge.write(f"**{row[2]}**")
    massge.write(f"{row[5]}")
    massge.write('---')