# 🎬 LSTM Movie Review Sentiment Analysis

A **Deep Learning NLP project** that classifies movie reviews as **Positive or Negative** using an **LSTM (Long Short-Term Memory) neural network**.
The trained model is deployed as an **interactive web application using Streamlit**.

---

# 🚀 Project Overview

Sentiment Analysis is a Natural Language Processing (NLP) technique used to determine the emotional tone behind text.

In this project, we build a **deep learning based sentiment classifier** that analyzes movie reviews and predicts whether the review expresses a **positive or negative sentiment**.

The model is trained on the **IMDB Movie Reviews Dataset (50,000 reviews)** and deployed as a **web app** so users can input their own reviews and instantly get predictions.

---

# 🧠 Model Architecture

The deep learning model is built using the following layers:

```
Text Input
   ↓
Tokenization
   ↓
Padding Sequences
   ↓
Embedding Layer
   ↓
LSTM Layer
   ↓
Dense Layer (Sigmoid)
   ↓
Sentiment Prediction
```

### Layers Used

* **Embedding Layer**
  Converts word indexes into dense vector representations.

* **LSTM Layer**
  Captures sequential patterns and context in text.

* **Dense Output Layer**
  Uses a **sigmoid activation** to classify sentiment.

---

# 📊 Dataset

Dataset used:

```
IMDB Movie Reviews Dataset
```

Dataset characteristics:

* **50,000 movie reviews**
* **Binary classification**
* Labels:

  * Positive
  * Negative

Dataset split:

```
Training Data : 80%
Testing Data  : 20%
```

---

# ⚙️ Technologies Used

* Python
* TensorFlow / Keras
* Scikit-learn
* Pandas
* NumPy
* Streamlit

---

# 📁 Project Structure

```
Sentiment_LSTM_App
│
├── app.py                     # Streamlit web application
├── lstm_sentiment_model.h5    # Trained LSTM model
├── tokenizer.pkl              # Saved tokenizer
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

---

# 🔧 Installation

Clone the repository:

```
git clone https://github.com/Rudra12426/lstm-sentiment-analyzer.git
```

Navigate to the project folder:

```
cd lstm-sentiment-analyzer
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# ▶️ Run the Application

Run the Streamlit app:

```
streamlit run app.py
```

The application will open in your browser:

```
http://localhost:8501
```

---

# 💻 Web App Features

The web application allows users to:

* Enter a movie review
* Process the text using the trained tokenizer
* Predict sentiment using the LSTM model
* Display results instantly

Example input:

```
"This movie was absolutely fantastic!"
```

Output:

```
Positive Review 😀
```

---

# 📈 Model Performance

Typical performance:

```
Accuracy: ~85% - 90%
```

The model learns contextual patterns in text using **LSTM networks**, making it more effective than traditional machine learning methods for sequential data.

---

# 🌐 Deployment

This project can be deployed online using **Streamlit Cloud**.

Steps:

1. Push project to GitHub
2. Connect repository to Streamlit Cloud
3. Deploy the app

Once deployed, the app can be accessed through a public URL.

---

# 🎯 Learning Outcomes

Through this project, I learned:

* Natural Language Processing fundamentals
* Text preprocessing and tokenization
* Sequence modeling with LSTM networks
* Deep learning model training with TensorFlow
* Saving and loading ML models
* Building web apps for ML models using Streamlit
* Deploying AI applications online

---

# 📌 Future Improvements

Possible enhancements:

* Use **Bidirectional LSTM**
* Improve model accuracy with **pretrained embeddings (GloVe / Word2Vec)**
* Add **attention mechanisms**
* Implement **transformer-based models**
* Improve UI design of the web app

---

# 👨‍💻 Author

**Rudra Pratap**

AI / Machine Learning Enthusiast
Building real-world AI projects and sharing my learning journey.

---

# ⭐ If you found this project useful

Consider giving the repository a **star ⭐** on GitHub!
