# python -m streamlit run strmlit.py
import streamlit as st

# Список книг
books = [
    {"Название": "Вишневый сад", "Автор": "Чехов Антон Павлович", "Жанр": "Комедия", "Магазин": "адрес 1"},
    {"Название": "Спать хочется", "Автор": "Чехов Антон Павлович", "Жанр": "Комедия", "Магазин": "адрес 2"},
    {"Название": "Книга 3", "Автор": "Автор 1", "Жанр": "Жанр 2", "Магазин": "адрес 2"},
    {"Название": "Книга 4", "Автор": "Автор 3", "Жанр": "Жанр 3", "Магазин": "Магазин 1"}
]


# Фильтрация книг по автору
def filter_books_by_author(books, author):
    return [book for book in books if book["Автор"] == author]


# Фильтрация книг по жанру
def filter_books_by_genre(books, genre):
    return [book for book in books if book["Жанр"] == genre]


# Фильтрация книг по магазину
def filter_books_by_store(books, store):
    return [book for book in books if book["Магазин"] == store]


# Добавление книги в корзину
def add_to_cart(book):
    cart = st.session_state.get("cart", [])
    cart.append(book)
    st.session_state["cart"] = cart


# Получение содержимого корзины
def get_cart_items():
    return st.session_state.get("cart", [])


# Очистка корзины
def clear_cart():
    st.session_state["cart"] = []


st.title("Дом Книги")
st.sidebar.header("Фильтры")

books_state = books

selected_author = st.sidebar.selectbox("Выберите автора", ["Все"] + list(set([book["Автор"] for book in books])))
if selected_author != "Все":
    books_state = filter_books_by_author(books_state, selected_author)

selected_genre = st.sidebar.selectbox("Выберите жанр", ["Все"] + list(set([book["Жанр"] for book in books])))
if selected_genre != "Все":
    books_state = filter_books_by_genre(books_state, selected_genre)

selected_store = st.sidebar.selectbox("Выберите магазин", ["Все"] + list(set([book["Магазин"] for book in books])))
if selected_store != "Все":
    books_state = filter_books_by_store(books_state, selected_store)


st.header("Книги")

if len(books_state) > 0:
    for book in books_state:
        st.write(f"**{book['Название']}**")
        st.write(f"Автор: {book['Автор']}")
        st.write(f"Жанр: {book['Жанр']}")
        st.write(f"Магазин: {book['Магазин']}")

        # Добавление в корзину
        if st.button("Добавить в корзину", key=book["Название"]):
            add_to_cart(book["Название"])
            st.success("Книга добавлена в корзину.")

        st.write("---")
else:
    st.write("Нет доступных книг.")

    # Корзина
st.sidebar.header("Корзина")
cart_items = get_cart_items()
for item in cart_items:
    st.sidebar.write(item)

cart_button = st.sidebar.button("Очистить корзину")

if cart_button:
    clear_cart()
    st.sidebar.success("Корзина очищена.")
