import pickle
import streamlit as st
import numpy as np

st.header("Book Recommender System using Machine Learning")
# load the model
model = pickle.load(open('artifacts/model.pkl', 'rb'))
books_name = pickle.load(open('artifacts/book_names.pkl', 'rb'))
final_rating = pickle.load(open('artifacts/dataset.pkl', 'rb'))
book_pivot = pickle.load(open('artifacts/book_pivot.pkl', 'rb'))

def truncate_title(title, max_length=16):
    if len(title) > max_length:
        return title[:max_length] + "..."
    return title

def fetch_cover(books):
    poster_url = []

    for book_id in books[0]:  # Iterate through the first row of suggestions
        book_title = book_pivot.index[book_id]
        url = final_rating[final_rating['Title'] == book_title]['Image'].values[0]
        poster_url.append(url)
    
    return poster_url

def recommend_books(name):
    """A function to use our model to recommend its most similar books using collaborative filtering"""
    book_list = []
    # fetch book id from the pivot table 
    book_id = list(book_pivot.index).index(name)
    # make the prediction to get the suggestions
    _ , suggestions = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors=6)

    # get the cover image link
    poster_url = fetch_cover(suggestions)
    
    for i, suggestion in enumerate(suggestions[0]):
        book = book_pivot.index[suggestion]
        book_list.append(book)
    return book_list, poster_url

# create a selecting box to choose the book
selected_book = st.selectbox(
    "Type or select a book",
    books_name
)

# create a submit button
if st.button("Show Recommendations"):
    # create the function that will make the recommendations 
    recommendation_books, poster_url = recommend_books(selected_book)
    print(recommendation_books)
    print(poster_url)
    # show the recommended books (excluding the book itself)
    # define 5 cols 
    col1, col2, col3, col4, col5 = st.columns(5)
    # rendering these cols 
    with col1:
        # define title of the book
        st.text(truncate_title(recommendation_books[1]))
        # define the cover image
        st.image(poster_url[1])
    with col2:
        # define title of the book
        st.text(truncate_title(recommendation_books[2]))
        # define the cover image
        st.image(poster_url[2])
    with col3:
        # define title of the book
        st.text(truncate_title(recommendation_books[3]))
        # define the cover image
        st.image(poster_url[3])
    with col4:
        # define title of the book
        st.text(truncate_title(recommendation_books[4]))
        # define the cover image
        st.image(poster_url[4])
    with col5:
        # define title of the book
        st.text(truncate_title(recommendation_books[5]))
        # define the cover image
        st.image(poster_url[5])
