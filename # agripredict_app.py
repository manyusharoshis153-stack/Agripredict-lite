# agripredict_app.py
import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
st.set_page_config(page_title="AgriPredict Lite", page_icon="🌱")

st.title("🌱 AgriPredict Lite")
st.markdown("**AI-Powered Crop Recommendation for Indian Farmers**")

df = pd.read_csv('crop_data.csv')

with st.expander("See the knowledge base we use"):
    st.dataframe(df)

st.header("🤔 What should I grow?")
st.subheader("Get a personalized crop recommendation")

state = st.selectbox("Select your State", df['State'].unique())
district = st.selectbox("Select your District", df[df['State'] == state]['District'].unique())
soil_type = st.selectbox("Select your Soil Type", df['Soil_Type'].unique())
rainfall = st.slider("Annual Rainfall (mm)", min_value=300, max_value=2500, value=1000)
temperature = st.slider("Average Temperature (°C)", min_value=10, max_value=35, value=25)

if st.button("Get Recommendation"):
    try:
        recommended_crop = df[(df['District'] == district) & (df['Soil_Type'] == soil_type)]['Crop'].iloc[0]
        st.success(f"**Recommended Crop:** {recommended_crop}")
    except:
        st.warning("Hmm, we don't have a specific recommendation for that combination yet. Our scientists are working on it!")

    st.info(f"Based on the data for {district} district, which has {soil_type.lower()} soil and a suitable climate for {recommended_crop}.")

st.header("📈 Yield Prediction (Experimental)")

crop_for_prediction = st.selectbox("Select a Crop to Predict Yield", df['Crop'].unique())
if st.button("Predict Yield"):
    simulated_yield = rainfall / 100 + (temperature * 2)
    st.metric(label="**Predicted Yield (Quintal/Hectare)**", value=f"{simulated_yield:.1f}")
    st.write("*(Disclaimer: This is a simulated prediction for demo purposes. A full model would use historical yield data.)*")

st.markdown("---")
st.markdown("Built with ❤️ for Smart India Hackathon using Streamlit.")