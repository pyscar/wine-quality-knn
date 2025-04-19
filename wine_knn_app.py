import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# Page setup
st.set_page_config(page_title="Wine Quality Prediction", layout="centered")
st.title("🍷 Wine Quality Predictor (KNN)")

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("WineQT.csv")

df = load_data()
st.write("### Sample of Dataset", df.head())

# Sidebar for user input
st.sidebar.header("Input Features")

def user_input():
    feature_cols = df.drop(columns=["quality", "Id"]).columns
    data = {}
    for col in feature_cols:
        data[col] = st.sidebar.slider(
            col,
            float(df[col].min()),
            float(df[col].max()),
            float(df[col].mean())
        )
    return pd.DataFrame(data, index=[0])

input_df = user_input()

# Prepare data for model
X = df.drop(columns=["quality", "Id"])
y = df["quality"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train KNN model
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

# Predict
input_scaled = scaler.transform(input_df)
prediction = model.predict(input_scaled)

# Display result
st.write("### Prediction")
st.success(f"The predicted wine quality is: **{int(prediction[0])}**")

#streamlit run wine_knn_app.py