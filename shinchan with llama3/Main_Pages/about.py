import streamlit as st

def show():
    st.title("About Us")
    st.write(" **Action beam hahahahahaha** ")
    st.image("shinchan/images/shinchan.jpg", width=100)
    st.markdown("<hr>", unsafe_allow_html=True)
    st.text('''
    Hello, I'm Shinchan Nohara
    Let's begin this delightful journey of Generative AI together!''')
    st.markdown("<br>", unsafe_allow_html=True)


    st.markdown('''
    ## Want to Learn Generative AI❓
    If you're looking to dive into **Generative AI in 2024** , explore my comprehensive roadmap designed to guide your learning journey.
    Click the button below to embark on an exciting exploration of Generative AI techniques and applications.
    Get ready to unleash your creativity and explore the cutting-edge of artificial intelligence.
    **Check out my Generative AI Roadmap** 👇
    ''')
    st.markdown("<br>", unsafe_allow_html=True)
    bt = st.link_button(url="https://github.com/Hurrahh/Generative-AI-Roadmap-for-2024",label="GENERATIVE AI ROADMAP")

    st.markdown( " #### Let's Connect")
    st.image("shinchan/images/Connect.png", use_column_width=True)
    st.markdown('''
    - **My Linkedln -** [LINKEDLN](www.linkedin.com/in/niket-singh-338b1a218) 
    - **My GitHub -**  [GITHUB](https://github.com/hurrahh) 
    ''')

