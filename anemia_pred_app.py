import streamlit as st
import pandas as pd

# Load tips from Excel
df = pd.read_csv("anemia status predictor.csv")  # Replace with the path to your Excel file

# Title
st.title("Anemia Detection and Health Suggestions")

# User Inputs
name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=0, max_value=120, value=20)
sex = st.selectbox("Select your sex", ["Female", "Male"])
hgb = st.number_input("Enter Hemoglobin Level (g/dL)", min_value=0.0, max_value=20.0, value=12.0)

# Button to process
if st.button("Check Anemia Status"):
    # Determine Anemia Level
    if hgb < 10:
        level = "severe anemia"
    elif hgb >= 10 and hgb <12:
          level = "moderate anemia"
    elif hgb >=12 and hgb <15:
        level = "mild anemia"
    else:
        level = "normal"

    # Fetch tips from the Excel file
    tip_row = df[df["Anemia level"]==level]
    if not tip_row.empty:
        food = tip_row.iloc[0]['food']
        supplements=tip_row.iloc[0]['supplements and lifestyle']
        tips = f"**Food:** {food}\n\n **supplements:** {supplements}"
    else:
        tips = "no tips found for this level."

    # Display Report
    st.subheader("Health Report")
    st.markdown(f"""
    *Name:* {name}  
    *Age:* {age}  
    *Sex:* {sex}  
    *Hemoglobin:* {hgb} g/dL  
    *Anemia Level:* {level}  

    *Recommendations:*  
    {tips}
    """)
