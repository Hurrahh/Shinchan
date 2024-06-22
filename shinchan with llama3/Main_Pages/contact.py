import streamlit as st
# import pymongo


# client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

# mydb = client['User']

# info = mydb.userinformation
def show():

    st.title("Contact Us")
    st.markdown("<br>", unsafe_allow_html=True)
    st.write(''' #### Reach out to us via the form below.''')
    form = st.form('contact_form')
    st.markdown("<br>", unsafe_allow_html=True)
    name = form.text_input("Name")
    email = form.text_input("Email")
    message = form.text_area("Message")
    st.markdown("<br>", unsafe_allow_html=True)
    button = form.form_submit_button("Submit")
    record = {
        'Name': name,
        'email': email,
        'message': message,
    }

    if button:
        # info.insert_one(record)
        st.success("Thank you! We will be in touch soon.")

