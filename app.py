import streamlit as st
import joblib
import sklearn

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Email Spam Detection",
    page_icon="📧",
    layout="centered"
)

# ----------------------------
# Load Model
# ----------------------------
model = joblib.load("Email_spam_model.pkl")

# ----------------------------
# Title
# ----------------------------
st.title("📧 Email Spam Detection")
st.write("Predict whether an email is **Spam** or **Not Spam** using Machine Learning.")


email = st.text_area(
    "Enter Email Text",
    height=250,
    placeholder="Type or paste your email here..."
)


# ----------------------------
# Prediction
# ----------------------------
if st.button("Predict"):

    if not email.strip():
        st.warning("Please enter an email message.")
    else:
        prediction = model.predict([email])[0]
            
        probability = model.predict_proba([email])[0]
        
        confidence = max(probability) * 100
        
        if prediction == 1:
            st.error("🚨 Spam Email")
            st.metric("Spam Confidence", f"{confidence:.2f}%")
        else:
            st.success("✅ Not Spam")
            st.metric("Not Spam Confidence", f"{confidence:.2f}%")
            st.progress(confidence / 100)

   