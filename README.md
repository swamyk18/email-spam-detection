# 📧 Email Spam Detection Using Machine Learning

## 📌 Project Overview

This project is a Machine Learning application that classifies email messages as **Spam** or **Not Spam (Ham)** using Natural Language Processing (NLP) techniques.

The project includes data preprocessing, text cleaning, feature extraction using TF-IDF, training multiple machine learning models, model evaluation, hyperparameter tuning using GridSearchCV, and saving the trained model using Joblib.

---

## 🚀 Features

- Email text preprocessing and cleaning
- Removal of punctuation and unwanted characters
- Text feature extraction using TF-IDF
- Label encoding for target classes
- Training and testing machine learning models
- Comparison of multiple classification algorithms
- Hyperparameter tuning using GridSearchCV
- Model evaluation using classification metrics
- Saving trained models using Joblib

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib
---

## 📂 Dataset

The project uses an email spam dataset containing text messages and their corresponding labels.

The dataset includes two categories:

- Spam
- Ham not (spam) 

The dataset is used to train and evaluate the machine learning models.

---

## 📊 Project Workflow

```text
Load Dataset
      │
      ▼
Data Exploration
      │
      ▼
Data Preprocessing
      │
      ▼
Text Cleaning
      │
      ▼
Label Encoding
      │
      ▼
Train-Test Split
      │
      ▼
TF-IDF Feature Extraction
      │
      ▼
Model Training
      │
      ├── Multinomial Naive Bayes
      ├── Decision Tree Classifier
      ├── K-Nearest Neighbors (KNN)
      └── Random Forest Classifier
      │
      ▼
Model Evaluation
      │
      ▼
Hyperparameter Tuning using GridSearchCV
      │
      ▼
Best Model Selection
      │
      ▼
Save Trained Model using Joblib
      │
      ▼
Spam Prediction on New Emails
```
## 📈 Evaluation Metrics

The machine learning models are evaluated using the following metrics:

- **Accuracy Score**
- **Classification Report** 
- **Confusion Matrix** 
---

## 📁 Project Structure

```text
email-spam-detection/
│
├── Text_data_pipeline.ipynb
├── email_spam.csv
├── spam_model.pkl
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/YourUsername/email-spam-detection.git
cd email-spam-detection
```

Replace `YourUsername` with your GitHub username.

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Open the Notebook

Open `Text_data_pipeline.ipynb` using Jupyter Notebook or Visual Studio Code.

### 4. Run the Notebook

Execute the notebook cells in order to preprocess the dataset, train the models, evaluate their performance, perform hyperparameter tuning, and save the selected model.

---

## 📦 Model Serialization

The trained model and label encoder are saved using Joblib so they can be loaded later for prediction without retraining.

Example:

```python
import joblib

model = joblib.load("spam_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")
```

**Note:** The saved model must receive input features in the same format used during training. If TF-IDF vectorization is used, the fitted vectorizer must also be saved and loaded for predictions on new email text.

---

## 📚 Concepts Covered

- Natural Language Processing (NLP)
- Text Preprocessing and Cleaning
- Regular Expressions
- TF-IDF Vectorization
- Label Encoding
- Supervised Machine Learning
- Classification Algorithms
- Model Evaluation
- GridSearchCV Hyperparameter Tuning
- Model Serialization using Joblib

---

## 🔮 Future Improvements

- Build a web application using Flask or Streamlit.
- Add real-time email spam prediction.
- Experiment with additional classification algorithms.
- Improve performance through feature engineering.
- Deploy the trained model as a prediction API.

---
## Author :
  **K Swamy**

