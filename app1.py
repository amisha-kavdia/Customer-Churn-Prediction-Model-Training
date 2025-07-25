import streamlit as st
import joblib
import pandas as pd

st.title("Customer Churn Prediction")
st.markdown("This app predicts whether a customer will churn based on the given details.")
st.header("Customer Input")

# --- Load model once ---
@st.cache_resource
def load_model():
    return joblib.load("Churn.pkl")

model = load_model()

# --- Sidebar inputs ---
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
senior_citizen = st.sidebar.selectbox("Senior Citizen", [0, 1])
partner = st.sidebar.selectbox("Partner", ["Yes", "No"])
dependents = st.sidebar.selectbox("Dependents", ["Yes", "No"])
tenure = st.sidebar.slider("Tenure (Months)", 0, 72, 1)
phone_service = st.sidebar.selectbox("Phone Service", ["Yes", "No"])
multiple_lines = st.sidebar.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
internet_service = st.sidebar.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
online_security = st.sidebar.selectbox("Online Security", ["Yes", "No", "No internet service"])
online_backup = st.sidebar.selectbox("Online Backup", ["Yes", "No", "No internet service"])
device_protection = st.sidebar.selectbox("Device Protection", ["Yes", "No", "No internet service"])
tech_support = st.sidebar.selectbox("Tech Support", ["Yes", "No", "No internet service"])
streaming_tv = st.sidebar.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
streaming_movies = st.sidebar.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
contract = st.sidebar.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
paperless_billing = st.sidebar.selectbox("Paperless Billing", ["Yes", "No"])
payment_method = st.sidebar.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
monthly_charges = st.sidebar.number_input("Monthly Charges", 0.0, 200.0, 50.0)
total_charges = st.sidebar.number_input("Total Charges", 0.0, 10000.0, 500.0)

# Put into DataFrame with the exact column names the pipeline was trained on
input_df = pd.DataFrame({
    "gender": [gender],
    "SeniorCitizen": [senior_citizen],
    "Partner": [partner],
    "Dependents": [dependents],
    "tenure": [tenure],
    "PhoneService": [phone_service],
    "MultipleLines": [multiple_lines],
    "InternetService": [internet_service],
    "OnlineSecurity": [online_security],
    "OnlineBackup": [online_backup],
    "DeviceProtection": [device_protection],
    "TechSupport": [tech_support],
    "StreamingTV": [streaming_tv],
    "StreamingMovies": [streaming_movies],
    "Contract": [contract],
    "PaperlessBilling": [paperless_billing],
    "PaymentMethod": [payment_method],
    "MonthlyCharges": [monthly_charges],
    "TotalCharges": [total_charges],

})

st.write("**Current Input**")
st.write(input_df)

def encode_inputs():
    yes_no = {"Yes": 1, "No": 0}
    contract_map = {
    'Month-to-month': 0,
    'One year': 1,
    'Two year': 2
}

    internet_map = {
    'DSL': 0,
    'Fiber optic': 1,
    'No': 2
}

    payment_map = {
    'Electronic check': 0,
    'Mailed check': 1,
    'Bank transfer (automatic)': 2,
    'Credit card (automatic)': 3
}
    data = {
        "gender": 1 if gender == "Male" else 0,
        "SeniorCitizen": senior_citizen,
        "Partner": yes_no[partner],
        "Dependents": yes_no[dependents],
        "tenure": tenure,
        "PhoneService": yes_no[phone_service],
        "MultipleLines": 0 if multiple_lines == "No phone service" else yes_no.get(multiple_lines, 0),
        "InternetService": internet_map[internet_service],
        "OnlineSecurity": 0 if online_security == "No internet service" else yes_no.get(online_security, 0),
        "OnlineBackup": 0 if online_backup == "No internet service" else yes_no.get(online_backup, 0),
        "DeviceProtection": 0 if device_protection == "No internet service" else yes_no.get(device_protection, 0),
        "TechSupport": 0 if tech_support == "No internet service" else yes_no.get(tech_support, 0),
        "StreamingTV": 0 if streaming_tv == "No internet service" else yes_no.get(streaming_tv, 0),
        "StreamingMovies": 0 if streaming_movies == "No internet service" else yes_no.get(streaming_movies, 0),
        "Contract": contract_map[contract],
        "PaperlessBilling": yes_no[paperless_billing],
        "PaymentMethod": payment_map[payment_method],
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges,
        }
    return pd.DataFrame([data])

if st.button("Predict Customer Churn"):
    input_df = encode_inputs()
    prediction = model.predict(input_df)
    label = "Churn" if prediction[0] == 1 else "Not Churn"
    st.subheader("Prediction")
    st.success(label)
