import streamlit as st
import pandas as pd

st.set_page_config(page_title="AgriPredict Lite", page_icon="🌱")
st.title("🌱 AgriPredict Lite")
st.markdown("**AI-Powered Crop Recommendation for Indian Farmers**")

try:
    df = pd.read_csv('crop_data.csv')
    st.success("Dataset loaded successfully!")
except FileNotFoundError:
    st.error("ERROR: 'crop_data.csv' file not found. Please make sure it is in the same folder as this script.")
    st.stop() 
with st.expander("Click to see the crop data we use"):
    st.dataframe(df)

st.header("🤔 What should I grow?")
state_list = df['State'].unique()
district_list = df['District'].unique()
soil_list = df['Soil_Type'].unique()

selected_state = st.selectbox("Select your State", state_list)
filtered_districts = df[df['State'] == selected_state]['District'].unique()
selected_district = st.selectbox("Select your District", filtered_districts)
selected_soil = st.selectbox("Select your Soil Type", soil_list)

if st.button("Get Recommendation"):
    result = df[(df['State'] == selected_state) & 
                (df['District'] == selected_district) & 
                (df['Soil_Type'] == selected_soil)]
    
    if not result.empty:
        recommended_crop = result['Crop'].iloc[0]
        st.balloons()
        st.success(f"**Recommended Crop: {recommended_crop}**")
        st.info(f"Based on data for {selected_district} district ({selected_state}), which has {selected_soil.lower()} soil.")
    else:
        st.warning("Sorry, we don't have a specific recommendation for that combination yet. Please try a different selection.")
st.header("📈 Yield Prediction (Experimental)")
crop_list = df['Crop'].unique()
selected_crop = st.selectbox("Select a Crop", crop_list)

if st.button("Predict Yield"):
    simulated_yield = (df[df['Crop'] == selected_crop]['Avg_Rainfall'].mean() / 100) + 10
    st.metric(label=f"**Predicted Yield for {selected_crop} (Quintal/Hectare)**", value=f"{simulated_yield:.1f}")
    st.caption("(Disclaimer: This is a simulated prediction for demo purposes.)")