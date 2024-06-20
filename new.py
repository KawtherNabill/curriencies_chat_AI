import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def get_currency_info(currency_name):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0.7,
        messages=[
            {"role": "system", "content": "You are an expert on digital currencies."},
            {"role": "user", "content": f"Tell me about the digital currency: {currency_name}"},
        ]
    )
    return response.choices[0].message.content

# Main page components
st.title("💰 Digital Currency Information")

currency_name = st.text_input("Enter the name of the digital currency:")
if st.button("Get Info"):
    if currency_name:
        response = get_currency_info(currency_name)
        st.markdown(response)
    else:
        st.markdown("Please enter a digital currency name.")

