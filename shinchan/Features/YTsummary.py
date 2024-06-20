from langchain_community.document_loaders import YoutubeLoader
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from translate import Translator


my_dict = {'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy':
'armenian', 'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', 'bn':
'bengali', 'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano',
'ny': 'chichewa', 'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)',
'co': 'corsican', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish', 'nl': 'dutch',
'en': 'english', 'eo': 'esperanto', 'et': 'estonian', 'tl': 'filipino', 'fi':'finnish',
'fr': 'french', 'fy': 'frisian', 'gl': 'galician', 'ka': 'georgian',
'de': 'german', 'el': 'greek', 'gu': 'gujarati', 'ht': 'haitian creole', 'ha': 'hausa',
'haw': 'hawaiian', 'iw': 'hebrew', 'he': 'hebrew', 'hi': 'hindi', 'hmn':'hmong',
'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 'id': 'indonesian',
'ga': 'irish', 'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada',
'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish (kurmanji)', 'ky': 'kyrgyz',
'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish', 'mk': 'macedonian',
'mg': 'malagasy', 'ms': 'malay', 'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi',
'mn': 'mongolian', 'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'or': 'odia',
'ps': 'pashto', 'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian',
'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho', 'sn': 'shona',
'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak','sl': 'slovenian', 'so': 'somali', 'es': 'spanish',
'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu',
'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian', 'ur': 'urdu', 'ug': 'uyghur',
'uz': 'uzbek', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu'}

# Initialize the LLM
llm=ChatGoogleGenerativeAI(model="gemini-1.0-pro",
                               verbose=True,
                               temperature=0.5,
                               google_api_key=st.secrets["GOOGLE_API_KEY"])

# Define the prompt template
prompt_template_str = '''You will be provided with a youtube video transcript.
Carefully read the transcript and prepare a thorough report of key facts and details.
Provide as many details and facts as possible in the summary.
Give the sections relevant titles and provide details/facts/processes in each section.

Transcript:
{transcript}
'''

prompt_template = PromptTemplate.from_template(template=prompt_template_str)
output_parser = StrOutputParser()

def extract_transcript_details(url):
    try:
        loader = YoutubeLoader.from_youtube_url(url, add_video_info=True)
        documents = loader.load()
        return "".join([doc.page_content for doc in documents]).strip()
    except Exception as e:
        print(f"Error extracting transcript: {e}")
        return None

def summary(transcript):
    prompt = prompt_template.format(
        transcript=transcript
    )

    response = llm.invoke(prompt)
    parsed_response = output_parser.parse(response)

    return parsed_response.content

def translate(transcript,language):
    chunks = [transcript[i:i+500] for i in range(0, len(transcript), 500)]
    if language in my_dict.values():
        lang = list(my_dict.keys())[list(my_dict.values()).index(language)]
        translator = Translator(to_lang=lang)
        translated_chunks = [translator.translate(chunk) for chunk in chunks]
        translated_text = ''.join(translated_chunks)
        return translated_text

    return None
def show():

    option = st.sidebar.radio("",['Generate Summary','Generate Transcript'])

    if option == "Generate Summary":
        st.title("YouTube Video Summarizer")
        youtube_link = st.text_input("📹Video URL")

        if st.button('Generate Summary'):
            with st.spinner("Generating..."):
                transcript_text = extract_transcript_details(youtube_link)
                if transcript_text:
                    response = summary(transcript_text)
                    st.write(response)
                else:
                    st.write("Sorry no transcript for this Video. Try for another video")
    else:
        st.title("Generate Transcript")
        youtube_link = st.text_input("📹Video URL")
        language = st.text_input('''To convert the transcript to another language, specify the language or leave blank for the original.''')

        if language and youtube_link and st.button("Generate"):
            with st.spinner('Generating...'):
                transcript = extract_transcript_details(youtube_link)
                response = translate(transcript,language)
                st.write(response)

        elif st.button('Generate') and not language:
            with st.spinner('Generating...'):
                transcript = extract_transcript_details(youtube_link)
                st.write(transcript)

