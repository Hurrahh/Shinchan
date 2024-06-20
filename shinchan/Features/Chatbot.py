from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st




history = []

def Generate(text):
    prompt = ChatPromptTemplate.from_messages(
            [
                ("system", "You are Shinchan Nohara, Now Provide response to the user queries"),
                ("user", "Question: {question}")
            ]
        )
    llm = ChatGoogleGenerativeAI(model = "gemini-1.5-flash",
                               verbose = True,
                               temperature = 0.5,
                               google_api_key = st.secrets["GOOGLE_API_KEY"])

    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser

    response = chain.invoke({'question':text})
    return response

def show():
    st.markdown('''
    # Conversational Bot Assistance
    ''')

    if chat_input:= st.chat_input("How can I assist you Today! "):
        with st.chat_message(name='user'):
            st.write(chat_input)
        with st.spinner("Generating..."):
            response = Generate(chat_input)
        with st.chat_message(name='AI'):
            st.write(response)
        history.append({'user':chat_input,'assistant':response})










