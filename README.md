# AI-Powered Market Basket Analysis Chatbot Using Streamlit and Cloud Hosting

## Abstract
This project builds an AI-powered chatbot that performs Market Basket Analysis (MBA) using association rule mining. The chatbot is built with Python and Streamlit, uses a CSV dataset for transaction data, and applies a custom Apriori algorithm without external ML libraries. It's designed for cloud hosting on platforms like Streamlit Cloud or Render.

## Why this is a Good AI + Cloud Mini Project

### 1. Artificial Intelligence Concepts
- **Association Rule Mining:** Implements unsupervised learning with Apriori algorithm.
- **Pattern Recognition:** Identifies frequent itemsets and makes intelligent product suggestions.
- **AI Chatbot:** Responds dynamically to user input with relevant recommendations.

### 2. Cloud Computing Concepts
- **Cloud Deployment:** Easily hosted using Streamlit Cloud or Render.
- **Serverless Hosting:** Infrastructure-free, scalable deployment.
- **Cloud Storage:** CSV data can be hosted on GitHub/Drive.
- **Real-Time Suggestions:** Provides instant responses via chatbot.

## Tech Stack
- **Frontend:** Streamlit
- **Backend:** Python (Custom Apriori)
- **Dataset:** CSV (Transaction data)
- **Hosting:** Streamlit Cloud / Render

## Project Structure
```
market-basket-chatbot/
├── data/
│   └── transactions.csv
├── chatbot.py
├── apriori.py
├── app.py
├── requirements.txt
└── README.md
```

## Sample Dataset (`transactions.csv`)
```
apple,banana,beer
apple,beer
banana,beer
apple,banana
apple,beer
banana,beer
```

## Key Files

### apriori.py
Contains functions to load transaction data, find frequent itemsets, and generate association rules using the Apriori algorithm.

### chatbot.py
Provides logic to fetch product suggestions based on user input and association rules.

### app.py
Streamlit UI where users input a product and receive recommendations based on past purchases.

### requirements.txt
```
streamlit
```

## Deployment Options

### Streamlit Cloud
1. Push code to a public GitHub repo.
2. Go to [https://share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo and deploy in one click.

### Render (Optional Advanced)
- Use Flask backend if needed.
- Embed chatbot in React if full-stack features are required.

## Conclusion
This chatbot demonstrates AI in action using pattern recognition and real-time recommendations. The use of cloud hosting ensures wide availability and zero-maintenance deployment—making it perfect for learning and educational showcases.
