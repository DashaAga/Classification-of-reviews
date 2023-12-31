from pickle import load
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def text_to_vector(text, vector_size=3816):
    # Создаем объект TF-IDF векторизатора с заданным размером
    vectorizer = TfidfVectorizer(max_features=vector_size, lowercase=True)

    # Преобразуем текст в TF-IDF вектор
    tfidf_vector = vectorizer.fit_transform([text])

    # Преобразуем разреженную матрицу в плотный массив
    dense_vector = tfidf_vector.toarray()

    # Если размер вектора меньше заданного, дополним нулями
    if dense_vector.shape[1] < vector_size:
        padding = np.zeros((1, vector_size - dense_vector.shape[1]))
        dense_vector = np.hstack((dense_vector, padding))

    return dense_vector


def load_model_and_predict(text, path="data/model.pickle"):
    with open(path, "rb") as file:
        model = load(file)
        prediction = model.predict(text_to_vector(text))
    return f"Вы бы поставили оценку {prediction}"
load_model_and_predict("оовыдлвзцвыз")