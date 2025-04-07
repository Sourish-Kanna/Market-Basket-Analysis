import streamlit as st
from apriori import load_transactions, get_frequent_itemsets, generate_rules
from chatbot import get_product_suggestions

st.title("🛒 AI Market Basket Analysis Chatbot")
st.subheader("Enter a product to get product recommendations")

@st.cache_data
def load_data():
    transactions = load_transactions("data/transactions.csv")
    frequent_itemsets, total = get_frequent_itemsets(transactions, min_support=0.01)
    rules = generate_rules(frequent_itemsets, total, min_confidence=0.01)
    return rules

rules = load_data()
user_input = st.text_input("Product name (e.g., cookies)").strip().lower()

if user_input:
    suggestions = get_product_suggestions(user_input, rules)
    if suggestions:
        st.success(f"Customers who bought '{user_input}' also bought:")
        for item, confidence in suggestions:
            st.markdown(f"- **{item}** (confidence: {confidence:.2f})")
    else:
        st.warning("No suggestions found for this product.")
