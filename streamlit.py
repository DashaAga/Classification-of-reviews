import pandas as pd
import streamlit as st
from PIL import Image
from workWithModel import load_model_and_predict

def process_main_page():
    show_main_page()
    process_inputs()

def show_main_page():
    image = Image.open('data/photo.jpg')

    st.set_page_config(
        layout="wide",
        page_title="Review Rating",
        page_icon=image,

    )

    st.write(
        """
        # Оставьте свой отзыв и получите его в числовом эквиваленте!
        """
    )

    st.image(image)


def write_prediction(prediction):
    st.write("## Предсказание")
    st.write(prediction)

def process_text_input(text):
    # Выводим текст на экран
    st.write("Вы ввели следующий текст:")
    st.write(text)

def process_inputs():
    st.write('Оставьте ваш отзыв')
    # Создаем поле для ввода текста
    user_input = st.text_input("Введите текст:")

    # Если пользователь ввел текст и нажал Enter
    if st.button("Обработать"):
        # Вызываем функцию для обработки текста
        process_text_input(user_input)
    text = st.text_input(value="Ваш отзыв")
    prediction = load_model_and_predict(text)
    write_prediction(prediction)


if __name__ == "__main__":
    process_main_page()