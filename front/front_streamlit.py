import streamlit as st
import requests
import os
import pandas as pd
from typing import Union
import plotly.express as px
import io
from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

backend_url = os.getenv("BACKEND_URL", "localhost:9797")


def send_prediction_request(data):
    url = "http://back-service:9797/predict" 
    response = requests.post(url, json={}, files={'file': data})
    st.write(response)
    return response.json()

def get_predictions(image_file):
    url = "http://back-service:9797/predict"
    response = send_prediction_request(image_file)
    return response


def main():
    st.header("osteoarthritis prediction :")
    st.text("""Upload your xray picture (jpeg format only)""")
    uploaded_file = st.file_uploader("", type=["jpg", "png"])
    if uploaded_file is not None:
        st.image(uploaded_file.getvalue())
        image = Image.open(uploaded_file)
        image_array = np.array(image)
        predictions = get_predictions(uploaded_file.getvalue())
        if predictions is not None:
            dfpred = pd.DataFrame(predictions.items(), columns=['Category', 'Probability'])
            df_boxplot = dfpred.copy()
            max_value = dfpred['Probability'].max()
            dfpred['Probability'] = dfpred['Probability'].apply(lambda x: 1 if x == max_value else 0)
            st.subheader("Results of osteoarthritis prediction")
            st.write("Prediction results:")
            st.dataframe(dfpred)

            fig, ax = plt.subplots(figsize=(8, 6))
            categories = df_boxplot['Category']
            probabilities = df_boxplot['Probability']
            bar_width = 0.5
            opacity = 0.8
            index = np.arange(len(categories))
            ax.bar(index, probabilities, bar_width, alpha=opacity)
            ax.set_xlabel('Category')
            ax.set_ylabel('Probability')
            ax.set_title('Predictions')
            ax.set_xticks(index)
            ax.set_xticklabels(categories)
            plt.tight_layout()
            st.pyplot(fig)

if __name__ == "__main__":
    main()
