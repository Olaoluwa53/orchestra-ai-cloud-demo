import streamlit as st
from router import call_phi3_groq, call_mixtral_together

st.set_page_config(page_title="Orchestra AI", page_icon="🤖")
st.title("🎼 Orchestra AI Support Assistant")

# Initialize session history
if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("Ask your question:", "")

if user_input:
    # Simple routing logic
    if len(user_input.split()) < 10:
        reply = call_phi3_groq(user_input)
        model_used = "Phi-3 via Groq"
    else:
        reply = call_mixtral_together(user_input)
        model_used = "Mixtral via Together"
    
    # Save to history
    st.session_state.history.append({
        "user": user_input,
        "reply": reply,
        "model": model_used
    })

# Display chat history
for entry in reversed(st.session_state.history):
    st.markdown(f"**You:** {entry['user']}")
    st.markdown(f"**{entry['model']} Response:** {entry['reply']}")
    st.markdown("---")
