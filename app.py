import streamlit as st
import numpy as np
import joblib
from sklearn.datasets import load_iris

@st.cache_resource
def load_model():
    return joblib.load("models/model.pkl")

def main():
    st.title("Iris Classifier - Streamlit demo")
    st.write("Enter iris features:")

    sepal_length = st.number_input("Sepal length (cm)", value=5.1, format="%.2f")
    sepal_width  = st.number_input("Sepal width (cm)",  value=3.5, format="%.2f")
    petal_length = st.number_input("Petal length (cm)", value=1.4, format="%.2f")
    petal_width  = st.number_input("Petal width (cm)",  value=0.2, format="%.2f")

    model = load_model()
    if st.button("Predict"):
        features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
        pred = model.predict(features)[0]
        iris = load_iris()
        st.success(f"Predicted: {iris.target_names[pred]} (label {pred})")

if __name__ == "__main__":
    main()
