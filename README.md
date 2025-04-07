# 🛒 Smart Market Basket Chatbot

A conversational AI chatbot that provides intelligent product recommendations based on market basket analysis using the Apriori algorithm. Built with **Streamlit** and powered by **association rules** mined from real-world transaction data.

![Streamlit Chatbot Screenshot](https://github.com/user-attachments/assets/3bd55382-867b-4848-abc3-8e4e476bc65c)

---

## 🚀 Features

- 💬 Conversational chatbot interface
- 🧠 NLP-based intent detection (e.g., "I need tea", "I want bread")
- 📈 Apriori-based market basket analysis for recommendations
- 🧺 Real transaction data support
- 🔁 Reset chat functionality
- 🧠 Similarity matching with fallback response
- ⚡ Built with Streamlit for quick deployment

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/market-basket-chatbot.git
cd market-basket-chatbot
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 🧠 How It Works

1. **User Input** — The chatbot interprets phrases like:
   - _"I need tea"_
   - _"Do you have cookies?"_
   - _"Give me bread"_

2. **NLP Matching** — Uses string similarity to map input to known products.

3. **Apriori Rules** — Applies association rules to suggest items often bought together.

4. **Bot Response** — Returns top product recommendations in conversational style.

---

## 📂 Project Structure

```bash
📁 market-basket-chatbot
├── app.py                 # Streamlit frontend
├── apriori.py             # Apriori algorithm & rule generation
├── chatbot.py             # NLP matching and suggestion logic
├── data/
│   └── transactions.csv   # Input data (real-world transactions)
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

---

## 📊 Example

> 🧑 You: I need tea  
> 🤖 Bot: People who bought **tea** also often bought: sugar, cookies, bread.

> 🧑 You: i want soap  
> 🤖 Bot: I didn’t quite get that. Try something like `I need milk`, `I want bread`.

---

## 📘 Requirements

- Python 3.8+
- Streamlit

Install all dependencies via:

```bash
pip install -r requirements.txt
```

---
