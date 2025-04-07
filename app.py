import streamlit as st
import streamlit.components.v1 as components
from apriori import load_transactions, get_frequent_itemsets, generate_rules
from chatbot import get_product_suggestions, best_match

@st.cache_data
def load_data():
    transactions = load_transactions("data/transactions.csv")
    frequent_itemsets, total = get_frequent_itemsets(transactions, min_support=0.01)
    rules = generate_rules(frequent_itemsets, total, min_confidence=0.5)
    product_set = {item for rule in rules for item in rule['antecedent'].union(rule['consequent'])}
    return rules, list(product_set)

# Load data
rules, products = load_data()

# Page UI
st.title("🛒 Smart Market Basket Chatbot")
st.markdown("Ask me something like `I need tea`, `Do you have bread?`, or `I want juice`. I'll suggest related products.")

# Chat history state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Reset chat
if st.button("🔄 Reset Chat"):
    st.session_state.chat_history = []
    st.rerun()

# Input form
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Type something like 'I need tea'...", key="input")
    submitted = st.form_submit_button("Send")

# JavaScript to refocus on text input after submission
components.html("""
<script>
    const input = window.parent.document.querySelector('input[type="text"]');
    if (input) {
        input.focus();
    }
</script>
""", height=0)

# Handle user input
if submitted and user_input:
    user_input_clean = user_input.strip().lower()

    # Handle greetings and exit
    if any(greet in user_input_clean for greet in ["hi", "hello", "help"]):
        bot_response = "Hey there! 👋 Ask me about a product and I’ll recommend related ones."
    elif "bye" in user_input_clean:
        bot_response = "Goodbye! 👋 Come back anytime."
    else:
        # Product match
        product, score = best_match(user_input_clean, products)
        if score >= 0.5:
            suggestions = get_product_suggestions(product, rules)
            if suggestions:
                bot_response = f"People who bought **{product}** also bought: {', '.join(suggestions[:5])}."
            else:
                bot_response = f"Hmm... I couldn’t find related items for **{product}**."
        else:
            bot_response = "I didn’t get that. Try something like `I need tea`, `I want bread`, or `Do you have juice?`"

    # Save chat
    # st.session_state.chat_history.append(("🧑 You", user_input))
    # st.session_state.chat_history.append(("🤖 Bot", bot_response))
    st.session_state.chat_history.append((user_input, bot_response))


# Display chat history (newest first)
for user_input, bot_response in reversed(st.session_state.chat_history):
    st.markdown(f"**🧑 You:** {user_input}")
    st.markdown(f"**🤖 Bot:** {bot_response}")
