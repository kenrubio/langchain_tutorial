import streamlit as st
from langchain.llms import OpenAI

st.title('🦜🔗Tutorial App')

openai_api_key = st.sidebar.text_input("OpenAI API Key")


def generate_response(input_text):
    llm = OpenAI(temperature=0.7, open_api_key=openai_api_key)
    
    # Displays the output in the webpage.
    st.info(llm(input_text))
    
with st.form("my_form"):
    
    # Displays the input in the webpage within a text box.
    text = st.text_area("Enter text:", "What is the name of your creator?")
    print("TEXT: ", text)

    # Creates a "Submit" button.
    submitted = st.form_submit_button("Submit")
    print("SUBMITTED: ", submitted)
   
    if not openai_api_key.startswith("sk-"):
        
        # Provides a warning pop-up when an error in the input is encountered.
        st.warning("Please enter your OpenAI API key.", icon="⚠")
        
    if submitted and openai_api_key.startswith("sk-"):
        generate_response(text)