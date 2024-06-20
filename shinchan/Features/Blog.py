import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

def getLLamaresponse(input_text, no_words, blog_style):
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                                 verbose=True,
                                 temperature=0.5,
                                 google_api_key=st.secrets["GOOGLE_API_KEY"])

    template = """
        Write a blog for {blog_style} job profile for a topic {input_text}
        within {no_words} words.
            """

    prompt = PromptTemplate(input_variables=["blog_style", "input_text", 'no_words'],
                            template=template)

    final_prompt = prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words)
    response = llm.invoke(final_prompt)
    return response.content


def show():
    st.header("Generate Blogs 🤖")

    input_text = st.text_input("Enter the Blog Topic")

    col1, col2 = st.columns([5, 5])

    with col1:
        no_words = st.text_input('No of Words')
    with col2:
        blog_style = st.selectbox('Writing the blog for',
                                  ('Researchers', 'Data Scientist', 'Common People'), index=0)

    submit = st.button("Generate")


    if submit:
        st.write(getLLamaresponse(input_text, no_words, blog_style))
