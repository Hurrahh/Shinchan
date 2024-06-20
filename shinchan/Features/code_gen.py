import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import streamlit as st
load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

history = []
def Generate(text):
    prompt1 = ChatPromptTemplate.from_messages(
            [
                ("system", "you are Shinchan Nohara,Now Generate code according to the user's need"),
                ("user", "prompt:{prompt}")
            ]
        )

    llm=ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest",
                               verbose=True,
                               temperature=1,
                               google_api_key=os.getenv("GOOGLE_API_KEY"))

    output_parser = StrOutputParser()
    chain = prompt1 | llm | output_parser

    response = chain.invoke({'prompt':text})
    return response

def show():
    st.markdown('''
    # Code Generator
    ''')

    if chat_input:= st.chat_input("How can I assist you Today! "):
        with st.chat_message(name='user'):
            st.write(chat_input)
        with st.spinner("Generating..."):
            response = Generate(chat_input)
        with st.chat_message(name='AI'):
            st.write(response)








