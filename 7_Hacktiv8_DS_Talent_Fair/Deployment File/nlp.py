import streamlit as st
import numpy as np
import pickle
import re
import tensorflow


# st.set_page_config(
#     page_title=">Auto Categorizing News Article",
#     page_icon="🧊",
#     # layout="wide",
#     initial_sidebar_state="expanded",
#     menu_items={
#         'Get Help': 'https://github.com/sonnyrd',
#         'Report a bug': "https://github.com/sonnyrd",
#         'About': "# >Auto Categorizing News Article"
#     }
# )

def app():
    #load style css
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
    local_css("style.css")

    #title
    st.write("<h1 style='text-align: center; '>📰Auto Categorizing News Article</h1>",
            unsafe_allow_html=True)


    # Baris 1

    article = st.text_area('Text to analyze',placeholder='Please input the article!',height=500)


    # # data preprocessing

    # Clean Text
    def clean_text(text):
        text = re.sub(r'<.*?>', ' ', text)
        text = re.sub('[^a-zA-Z]',' ',text)
        text = ' '.join(text.split())
        text = text.lower()
        return text

    data = clean_text(article)

    # tokenizer
    with open('tokenizer.pkl', 'rb') as f:
        tokenizer = pickle.load(f)

    data = tokenizer.texts_to_sequences([data])

    # padding
    data = tensorflow.keras.preprocessing.sequence.pad_sequences(data, maxlen=683)


    # load model
    model = tensorflow.keras.models.load_model('model_best.hdf5')

    # Predict
    if st.button('Predict'):
        if len(article) != 0:
            pred = model.predict(data)
            pred = np.argmax(pred,axis=1)
            with open('labelencoder.pkl', 'rb') as f:
                le = pickle.load(f)
            st.write(f"<h1 style='text-align: center; '>{str(le.inverse_transform(pred)[0])}</h1>", unsafe_allow_html=True)
        
        else:
            st.write('Error! Please insert the article first....')

    
