import streamlit as st
import time

# Title
st.title("🍽️ Smart Food Ordering App")
st.caption("Order your favorite food easily")

# User Info
st.subheader("👤 User Details")

name = st.text_input("Full Name", placeholder="First  Middle  Last")
city = st.selectbox("City", ["Ahmedabad", "Mumbai", "Delhi", "Bangalore"])
department = st.text_input("Department")
gender = st.radio("Gender", ["Male", "Female", "Other"])

# Food Section
st.subheader("🍕 Food Preference")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🍔 Food Items")
    food_choice = st.multiselect("Choose food", ["Pizza", "Burger", "Pasta"])

with col2:
    st.markdown("### 🥤 Beverages")
    beverage_choice = st.multiselect("Choose beverage", ["Coke", "Juice", "Coffee", "Milkshake"])

# Sidebar
st.sidebar.header("📊 Order Settings")
orders = st.sidebar.slider("How many times do you order food?", 1, 20, 2)

# DOB
st.subheader("📅 Personal Info")
dob = st.date_input("Date of Birth")

# Audio
st.subheader("🎤 Audio Message")
audio_message = st.audio_input("Record your message")

if audio_message:
    st.success("✅ Message recorded")
    st.audio(audio_message)

# Feedback
st.subheader("💬 Feedback")
feedback = st.text_area("Extra comments")

# Agreement
agree = st.checkbox("I agree to terms & conditions")

# Submit Button (Single clean flow)
if st.button("🚀 Place Order", use_container_width=True):

    # Validation
    if not name:
        st.warning("⚠️ Please enter your name")

    elif not agree:
        st.error("❌ Please accept terms & conditions")

    elif not food_choice:
        st.warning("🍽️ Please select at least one food item")

    else:
        # Loader (better than balloons/snow)
        with st.spinner("Placing your order..."):
            time.sleep(2)

        st.success(f"🎉 Order placed successfully, {name}!")
        st.toast("🛍️ Your food is on the way 🚴‍♂️")
        st.balloons()



