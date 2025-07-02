import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load data
df = pd.read_csv("anemia status predictor1.csv")

# Prepare data for ML
features = ['Age', 'Sex', 'HGB']  # Use relevant features
df['Sex'] = df['Sex'].map({'female': 0, 'male': 1})  # Encode sex
X = df[features]
y = df['Anemia level']

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Streamlit UI
st.title("Anemia Detection and Health Suggestions")

name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=0, max_value=120, value=20)
sex = st.selectbox("Select your sex", ["Female", "Male"])
hgb = st.number_input("Enter Hemoglobin Level (g/dL)", min_value=0.0, max_value=20.0, value=12.0)

if st.button("Check Anemia Status"):
    # Prepare input for prediction
    sex_num = 0 if sex == "Female" else 1
    input_data = pd.DataFrame([[age, sex_num, hgb]], columns=features)
    level = model.predict(input_data)[0]

    # Fetch tips
    tip_row = df[df["Anemia level"] == level]
    if not tip_row.empty:
        food = tip_row.iloc[0].get('food', 'N/A')
        supplements = tip_row.iloc[0].get('supplements', 'N/A')
    else:
        food = 'N/A'
        supplements = 'N/A'

    # Display
    st.subheader("Health Report")
    report = f"""
Name: {name}
Age: {age}
Sex: {sex}
Hemoglobin: {hgb} g/dL
Anemia Level: {level}

<<<<<<< HEAD:anemia_pred app.py
Recommendations:
Food: {food}
Supplements: {supplements}
"""
    st.markdown(report.replace('\n', '  \n'))  # For line breaks in markdown

    # Download button
    st.download_button(
        label="Download Health Report",
        data=report,
        file_name="health_report.txt",
        mime="text/plain"
    )
=======
    *Recommendations:*  
    {tips}
    """)
>>>>>>> baa747658e4ed5092580d16960ae04a201b13787:anemia_pred_app.py
