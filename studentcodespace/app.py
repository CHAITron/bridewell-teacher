import streamlit as st
import json

# Blue Buttons CSS
st.markdown("""
    <style>
    div.stButton > button {
        background-color: #27BFD6 !important;
        color: white !important;
        border: none !important;
        border-radius: 5px;
    }
    div.stButton > button:hover {
        background-color: #1D9AAD !important;
        color: white !important;
    }
    button[kind="primary"] {
        background-color: #27BFD6 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Initialisation
if "sessions" not in st.session_state:
    st.session_state.sessions = [{
        "id": 0, 
        "name": "Line of Questioning 1", 
        "messages": [],
        "analytics": {"rephrase": 0, "simplify": 0, "hint": 0, "topic": "None yet"}
    }]
if "active_session_idx" not in st.session_state:
    st.session_state.active_session_idx = 0
if "overall_analytics" not in st.session_state:
    st.session_state.overall_analytics = {"rephrase": 0, "simplify": 0, "hint": 0, "total_sessions": 1}

def log_event(action, label):
    st.session_state.overall_analytics[action] += 1
    active_idx = st.session_state.active_session_idx
    st.session_state.sessions[active_idx]["analytics"][action] += 1
    st.session_state.sessions[active_idx]["messages"].append({
        "role": "user", 
        "content": f"[Student clicked: {label}]"
    })

def create_new_chat():
    new_id = len(st.session_state.sessions)
    # Keeping internal name formal for the JSON
    new_name = f"Line of Questioning {new_id + 1}"
    st.session_state.sessions.append({
        "id": new_id, 
        "name": new_name, 
        "messages": [],
        "analytics": {"rephrase": 0, "simplify": 0, "hint": 0, "topic": "None yet"}
    })
    st.session_state.active_session_idx = new_id
    st.session_state.overall_analytics["total_sessions"] += 1
    st.rerun()

st.set_page_config(page_title="Student AI Interface", layout="centered")

# Sidebar for History - Using .replace() for student view
with st.sidebar:
    st.header("History")
    for i, session in enumerate(st.session_state.sessions):
        # Student sees "Chat X" instead of "Line of Questioning X"
        display_name = session['name'].replace("Line of Questioning", "Chat")
        
        if i == st.session_state.active_session_idx:
            st.button(f"-> {display_name}", key=f"sess_{i}", use_container_width=True)
        else:
            if st.button(display_name, key=f"sess_{i}", use_container_width=True):
                st.session_state.active_session_idx = i
                st.rerun()

# Main Page Action
if st.button("Start New Chat", use_container_width=True):
    create_new_chat()

active_session = st.session_state.sessions[st.session_state.active_session_idx]

# Make the Title 'Chat'
st.title(active_session["name"].replace("Line of Questioning", "Chat"))

# Chat Display
chat_container = st.container(height=500, border=True)
with chat_container:
    if not active_session["messages"]:
        st.info("Ask your first question to begin.")
    for msg in active_session["messages"]:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

# Dummy Responses
def get_dummy_response(action):
    responses = {
        "chat": "LLM Response: This is a general answer to your question.",
        "rephrase": "Rephrased Answer: This is the same information stated in a different way.",
        "simplify": "Simplified Answer: This is a simpler explanation of the previous point.",
        "hint": "Hint: Consider the relationship between the two main variables discussed."
    }
    return responses.get(action, "LLM Response")

# Input Logic
if prompt := st.chat_input("Type your message here..."):
    if active_session["analytics"]["topic"] == "None yet":
        active_session["analytics"]["topic"] = prompt
    active_session["messages"].append({"role": "user", "content": prompt})
    active_session["messages"].append({"role": "assistant", "content": get_dummy_response("chat")})
    st.rerun()

# Action Buttons
if active_session["messages"]:
    st.write("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Rephrase Answer", use_container_width=True):
            log_event("rephrase", "Rephrase Answer")
            active_session["messages"].append({"role": "assistant", "content": get_dummy_response("rephrase")})
            st.rerun()
    with col2:
        if st.button("Simplify Answer", use_container_width=True):
            log_event("simplify", "Simplify Answer")
            active_session["messages"].append({"role": "assistant", "content": get_dummy_response("simplify")})
            st.rerun()
    with col3:
        if st.button("Get a Hint", use_container_width=True):
            log_event("hint", "Get a Hint")
            active_session["messages"].append({"role": "assistant", "content": get_dummy_response("hint")})
            st.rerun()

# Analytics Sidebar
with st.sidebar:
    st.write("---")
    if st.checkbox("Show Backend JSON Payload"):
        analytics_payload = {"All Analytics": st.session_state.overall_analytics}
        for sess in st.session_state.sessions:
            analytics_payload[f"{sess['name']} Analytics"] = sess["analytics"]
        chat_data = {sess["name"]: sess["messages"] for sess in st.session_state.sessions}
        st.json({"Analytics": analytics_payload, "Chat": chat_data})