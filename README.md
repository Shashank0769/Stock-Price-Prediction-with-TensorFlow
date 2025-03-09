# 📈 Stock Price Prediction with TensorFlow & Streamlit

This project predicts the next day's stock price using a simple machine learning model built with **TensorFlow** and deployed using **Streamlit**.

---

## 🚀 Features
- Fetches **real-time stock data** from Yahoo Finance (`yfinance`)
- Uses **TensorFlow** to train a simple model
- Predicts the **next day's stock price**
- Interactive **Streamlit UI** with user input

---

## 🛠️ Installation

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/YOUR_USERNAME/Stock_price_prediction.git
cd Stock_price_prediction
```

### **2️⃣ Create a Virtual Environment**
```sh
python -m venv venv
venv\Scripts\activate    # Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

---

## 📊 Usage
### **Run the Streamlit App**
```sh
streamlit run app.py
```

### **Enter Stock Symbol & Date Range**
- Example: `GOOGL`, `AAPL`, `TSLA`
- Choose a date range
- Click **"Predict"** to see the next day's price

---

## 📂 Project Structure
```
Stock_price_prediction/
│── venv/                # Virtual environment (ignored in Git)
│── app.py               # Main application file
│── requirements.txt     # Required Python packages
│── README.md            # Project documentation
│── .gitignore           # Ignored files
```

---

## 🌐 Deployment on Streamlit Cloud
1. Push your project to GitHub
2. Go to [Streamlit Cloud](https://share.streamlit.io/)
3. Connect your GitHub repo
4. Deploy and share your app!

---

![Screenshot 2025-03-09 192554](https://github.com/user-attachments/assets/c816b875-7f52-413f-83f9-ce8ce7ccaa0b)


## 💡 Future Enhancements
- Implement **LSTM model** for better accuracy
- Add **multiple stock predictions** in one go
- Improve UI with **charts & graphs**

---

## 🤝 Contributing
Feel free to fork the repository, improve the code, and submit pull requests!

---

## 📜 License
This project is open-source under the **MIT License**.

