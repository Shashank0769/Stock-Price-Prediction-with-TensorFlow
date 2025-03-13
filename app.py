import streamlit as st
import tensorflow as tf
import numpy as np
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
import time

# Title
st.title("📈 Stock Price Prediction with TensorFlow")

# User Input for Stock Symbol
stock_symbol = st.text_input("Enter Stock Symbol (e.g., GOOGL, AAPL):", "GOOGL")

# Date Inputs
start_date = st.date_input("Start Date", value=None)
end_date = st.date_input("End Date", value=None)

# Predict Button
if st.button("Predict Next Day's Price"):
    progress_bar = st.progress(0)  # Initialize inside the button click event
    status_text = st.empty()  # Placeholder for status updates

    status_text.text("📡 Fetching stock data...")
    progress_bar.progress(10)
    time.sleep(0.5)  # Simulate loading time

    try:
        # Fetch stock prices
        data = yf.download(stock_symbol, start=start_date, end=end_date, interval="1d")
        progress_bar.progress(30)
        status_text.text("📊 Processing data...")
        time.sleep(0.5)

        stock_prices = data['Close'].values.astype(np.float32)
        if len(stock_prices) == 0:
            st.error("No data found. Try different dates.")
            progress_bar.empty()
        else:
            stock_prices = stock_prices[~np.isnan(stock_prices)]
            scaler = MinMaxScaler(feature_range=(0, 1))
            stock_prices_scaled = scaler.fit_transform(stock_prices.reshape(-1, 1))
            progress_bar.progress(50)

            # Prepare training data
            x_train = np.arange(len(stock_prices_scaled)).reshape(-1, 1)
            y_train = stock_prices_scaled

            # Define the model
            model = tf.keras.Sequential([
                tf.keras.layers.Input(shape=(1,)),
                tf.keras.layers.Dense(units=1)
            ])

            status_text.text("🤖 Training model...")
            progress_bar.progress(70)
            time.sleep(0.5)

            model.compile(optimizer='adam', loss='mean_squared_error')
            model.fit(x_train, y_train, epochs=1000, verbose=1)  # Set verbose=0 to avoid clutter
            progress_bar.progress(90)

            # Predict next day's stock price
            next_day = np.array([[len(stock_prices_scaled)]])
            predicted_price_scaled = model.predict(next_day)
            predicted_price = scaler.inverse_transform(predicted_price_scaled.reshape(-1, 1))

            # Display Prediction
            progress_bar.progress(100)
            status_text.text("✅ Prediction complete!")
            st.success(f"📊 Predicted next day's stock price for {stock_symbol}: ${predicted_price[0][0]:.2f}")
            
    except Exception as e:
        st.error(f"An error occurred: {e}")
        progress_bar.empty()
