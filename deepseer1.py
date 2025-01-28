import streamlit as st
from openai import OpenAI

# Initialize with DeepSeek's endpoint and your key
client = OpenAI(
    api_key="sk-c14b13afaffb41469de403d009953e16",  # Replace with your actual key
    base_url="https://api.deepseek.com/v1"  # Critical: Use /v1 endpoint
)

# Set page title and icon
st.set_page_config(page_title="Building your DeepSeek R1 personal investment porfolio", page_icon="🤖")
# Add DeepSeek logo
try:
    st.image("/Users/trangpham/Code/deepseek/deepseek-logo.jpg", width=200)  # Ensure the logo is in the same directory as your script
except FileNotFoundError:
    st.error("Logo file not found. Please ensure 'deepseek_logo.png' is in the correct directory.")
# App title
st.title("Building your DeepSeek R1 personal investment porfolio")

# Chat input
user_input = st.text_area("Your Message:", height=100)

# Send button
if st.button("Send"):
    if user_input.strip():  # Check if the input is not empty
        try:
            # Call the OpenAI API
            api_response = client.chat.completions.create(
                model="deepseek-reasoner",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant in segmentation and analytic in personal investment porfolio."},
                    {"role": "user", "content": user_input},
                ]
            )
            response = api_response.choices[0].message.content
            st.success("Response received!")
            st.write(response)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a message.")