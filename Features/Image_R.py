from PIL import Image
import io
import streamlit as st
import google.generativeai as genai


genai.configure(api_key=os.st.secrets["GOOGLE_API_KEY"])
def get_image_bytes(image_file):
    image_path = image_file
    image = Image.open(image_path)

    return image
    # with io.BytesIO() as output:
    #     image.save(output, format="png")
    #     image_bytes = output.getvalue()
    # return image_bytes

def stream_parser(stream):
    for data in stream:
        if data.get('response'):
            yield data['response']
        if data.get('done'):
            break

def generate_desc(file,prompt):
    image = get_image_bytes(file)
    llm = genai.GenerativeModel("gemini-pro-vision")
    stream = llm.generate_content([prompt, image])
    stream.resolve()
    return stream.text

def show():

    option = st.sidebar.radio("",['Image Description','Caption Generator'])

    if option == 'Image Description':
        st.title("Generate Description for the Image")
        file = st.file_uploader("Choose a image to Upload")
        prompt = st.text_input("Enter your prompt here")
        btn = st.button('Submit')

        if file and prompt and btn:
            st.image(file,use_column_width=True)
            with st.spinner('Generating Description...'):
                response = generate_desc(file,prompt)
                st.write(response)
    else:
        st.title("Generate Captions for your image")
        file = st.file_uploader("Choose a image to Upload")
        # st.image(file,width=300)
        if st.button("Generate") and file:
            with st.spinner("Generating caption..."):
                prompt = "Craft a captivating caption for this image suitable for social media posts or stories on platforms like Instagram and Facebook."
                desc = generate_desc(file,prompt)
                st.write(desc)
