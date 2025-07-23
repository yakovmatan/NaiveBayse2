import streamlit as st
import requests

URL_FEATURES = "http://127.0.0.1:8000/features"
URL_PREDICT = "http://127.0.0.1:8001/prediction"


@st.cache_data
def get_features_info():
    res = requests.get(URL_FEATURES)
    if res.ok:
        return res.json()["features"]
    else:
        st.error("❌ Error retrieving features from the server.")
        return {}


def predict_single_row(features_info):
    st.subheader("Enter values for each feature:")
    user_input = {}

    for feature, allowed_vals in features_info.items():
        user_input[feature] = st.selectbox(f"{feature}", allowed_vals)

    if st.button("Predict"):
        res = requests.post(URL_PREDICT, json=user_input)
        if res.ok:
            prediction = res.json().get("prediction")
            st.success(f"✅ Prediction result: {prediction}")
        else:
            st.error("❌ Failed to send request to the prediction server.")


st.set_page_config(page_title="Prediction App", layout="centered", page_icon="🤖")

st.title("🤖 Machine Learning Prediction App")

features_info = get_features_info()

if features_info:
    predict_single_row(features_info)
else:
    st.warning("No feature information retrieved from server.")
