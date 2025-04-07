import streamlit as st
from apriori import load_transactions, get_frequent_itemsets, generate_rules
from chatbot import get_product_suggestions

@st.cache_data
def load_data():
    transactions = load_transactions("data/transactions.csv")
    frequent_itemsets, total = get_frequent_itemsets(transactions, min_support=0.01)
    rules = generate_rules(frequent_itemsets, total, min_confidence=0.5)
    return rules

# Title
st.title("🛒 Smart Market Basket Chatbot")
st.markdown("Ask me about a product (e.g., `bread`, `tea`, `juice`) and I’ll suggest related items based on shopping patterns.")

rules = load_data()

# Store chat history
if "chat" not in st.session_state:
    st.session_state.chat = []

# Input box
user_input = st.text_input("Type a product name...", key="input")

# Process input
if user_input:
    suggestions = get_product_suggestions(user_input.strip().lower(), rules)
    if suggestions:
        top_suggestions = suggestions[:5]
        response = f"People who bought **{user_input}** also often bought: {', '.join(top_suggestions)}."
    else:
        response = f"🤔 Sorry, I couldn't find any frequent products related to **{user_input}**. Try something like 'bread', 'milk', or 'coffee'."

    # Save to chat history as a pair (user, bot)
    st.session_state.chat.insert(0, (user_input, response))


# Display chat history (most recent on top, user first then bot)
for user_msg, bot_msg in st.session_state.chat:
    st.markdown(f"**🧑 You:**  {user_msg}")
    st.markdown(f"**🤖 Bot:**  {bot_msg}")

