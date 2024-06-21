import streamlit as st
from Features import Blog, Chatbot, code_gen, Image_R, PDF_QA, YTsummary
from Main_Pages import about, home, contact

st.set_page_config(
    page_title="Shinchan",
    page_icon="🤖",

)

def tabs():
    t1,t2,t3 = st.tabs(['Home','About','Contact'])

    with t1:
        home.show()
    with t2:
        about.show()
    with t3:
        contact.show()

pages = {
    "Main": tabs,
    "Chat Bot": Chatbot,
    "Code Generator": code_gen,
    "Youtube Summarizer": YTsummary,
    "Document Q/A": PDF_QA,
    "Image": Image_R,
    "Blog Generation": Blog
}

st.sidebar.image("images/main.png", use_column_width=True)
st.sidebar.title("Shinchan")
page = st.sidebar.selectbox("Select Feature", list(pages.keys()))




if page == 'Main':
    tabs()
else:
    pages[page].show()



