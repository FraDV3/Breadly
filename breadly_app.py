import streamlit as st

# --- Basic App Information ---
st.set_page_config(page_title="Breadly - Your Sourdough Companion", page_icon="🍞", layout="centered")

# --- Custom CSS Styling ---
st.markdown("""
    <style>
        .main {
            background-color: #f0f0f0;
            padding: 20px;
            border-radius: 10px;
        }
        .title {
            text-align: center;
            font-size: 32px;
            color: #3a3a3a;
        }
        .description {
            text-align: center;
            font-size: 18px;
            color: #5a5a5a;
            margin-bottom: 30px;
        }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar Navigation ---
st.sidebar.title("Breadly - Your Sourdough Companion")
menu = st.sidebar.radio("Navigate", ["Home", "Starter Management", "Troubleshooting", "Baking Timer"])

# --- Home Page ---
if menu == "Home":
    st.markdown('<div class="main">', unsafe_allow_html=True)
    
    st.markdown('<div class="title">🍞 Breadly - Your Sourdough Companion</div>', unsafe_allow_html=True)
    st.markdown('<div class="description">Effortlessly manage your sourdough starters, troubleshoot issues, and schedule your perfect baking process.</div>', unsafe_allow_html=True)
    
    st.write("""
    **Features:**  
    - 🥖 Starter Management: Track feeding schedules, growth, and health of your sourdough starters.  
    - 🧐 Troubleshooting: Get help with common bread-making issues.  
    - ⏰ Baking Timer: Plan your bulk fermentation and proofing timings effectively.  
    - 📊 Visual Progress Tracker (Coming Soon!)  
    """)
    
    st.markdown('</div>', unsafe_allow_html=True)

# --- Starter Management Page ---
elif menu == "Starter Management":
    st.title("🥖 Starter Management")
    st.write("Track your sourdough starter feeding schedules and growth.")
    
    # Inputs for tracking starter feeding
    starter_name = st.text_input("Starter Name", value="My Sourdough Starter")
    last_feed = st.date_input("Last Feeding Date")
    feed_ratio = st.text_input("Feeding Ratio (e.g., 1:1:1)")

    if st.button("Save Starter Info"):
        st.success(f"Saved details for {starter_name}!")

# --- Troubleshooting Page ---
elif menu == "Troubleshooting":
    st.title("🧐 Troubleshooting")
    st.write("Find solutions to common sourdough problems.")
    
    issue = st.selectbox("Select an issue you're facing", [
        "My starter is not rising",
        "My bread is too dense",
        "My bread is too sour",
        "My crust is too thick",
        "My bread is too dry"
    ])

    if st.button("Get Help"):
        st.info(f"Showing solutions for: {issue}")

# --- Baking Timer Page ---
elif menu == "Baking Timer":
    st.title("⏰ Baking Timer")
    st.write("Manage your baking schedule effectively.")
    
    bulk_time = st.number_input("Bulk Fermentation Time (in hours)", min_value=1, max_value=24, value=4)
    proof_time = st.number_input("Proofing Time (in hours)", min_value=1, max_value=24, value=2)

    if st.button("Start Timer"):
        st.success(f"Baking schedule saved: Bulk - {bulk_time} hours, Proofing - {proof_time} hours.")