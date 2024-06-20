import streamlit as st
def show():
    st.title("Welcome to ShinChan 👋")
    st.write("Welcome to our website!")
    st.image("shinchan/images/shinchan2.jpg", width=100)
    st.markdown("<hr>", unsafe_allow_html=True)

    features = st.selectbox(
        'Select A feature',
        ['Conversational ChatBot',
         'Code Generation',
         'Image Description/Generation',
         'YouTube Video Summarization',
         'Document/PDF Q/A',
         'Blog Generation'
         ]
    )

    if features == "Conversational ChatBot":
        st.markdown(''' ## Conversational Bot Assistance''')
        st.image('shinchan/images/Chatbot.png',use_column_width=True)
        st.markdown('''
        - **Description:** A smart conversational bot ready to help you with any queries or issues, offering seamless interaction and support.
        Enter your prompt and chat with the assistant.
        
        - **Example Prompt:** "Can you help me troubleshoot my internet connection issues?"
        ''')
    elif features == "Code Generation":
        st.markdown(" ## Code Generation")
        st.image('shinchan/images/Code.png', use_column_width=True)
        st.markdown('''
        - **Description:** Effortlessly generate code snippets and solutions for various programming needs, saving you time and effort.
        You can specify in which language you want to generate code.
        
        - **Example Prompt:** "Generate a Python function to sort a list of dictionaries by a key."
        ''')
    elif features == "Image Description/Generation":
        st.markdown(" ## Image Description/Generation")
        st.image('shinchan/images/Image.png', use_column_width=True)
        st.markdown('''
        - **Description:** Obtain detailed descriptions of any image, making visual content more accessible and understandable.
        First Upload the Image and then write prompt 
        - **Description2:** You can generate Images
        
        - **Example Prompt:** "Describe the image of a sunset over the mountains."
        - **Example Prompt:** "Which food item in this image."
        ''')
    elif features == "YouTube Video Summarization":
        st.markdown(" ## YouTube Video Summarization")
        st.image('shinchan/images/Video.png', use_column_width=True)
        st.markdown('''
        - **Description:** YouTube Video Summarization
        Quickly get concise summaries of YouTube videos by providing the video link, helping you grasp key points without watching the entire video.
        Enter the Youtube Link, you can also specify your prompt
        
        - **Example Prompt:** "Summarize the main points of this YouTube video."
        ''')
    elif features == "Document/PDF Q/A":
        st.markdown("## Document/PDF Upload and Question Answering")
        st.image('shinchan/images/Document.png', use_column_width=True)
        st.markdown('''
        - **Description:** Document/PDF Question Answering
        Upload any document or PDF and ask questions about its content, receiving accurate and relevant answers instantly.
        
        - **Example Prompt:** "I’ve uploaded a PDF of my course syllabus. What are the main topics covered in week 3?"
        - **prompt2:** "I’ve uploaded a research paper on climate change. Can you summarize the key findings?"
        - **Prompt3:** "I’ve uploaded my resume. Can you identify any areas that need improvement?"
        ''')
    elif features == "Blog Generation":
        st.markdown(" ## Blog Generation")
        st.image('shinchan/images/Blog.png', use_column_width=True)
        st.markdown('''
        - **Description:** Create engaging blog posts on any topic. Provide a topic or a brief outline, and receive a well-structured article.
        
        - **Example Prompt:** "Write a blog post about the Generative AI Future Trends."
        ''')
