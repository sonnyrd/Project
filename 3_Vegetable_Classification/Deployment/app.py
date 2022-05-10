import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image
import requests
from io import BytesIO

st.set_page_config(
    page_title="Vegetable Image CLassification",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/sonnyrd',
        'Report a bug': "https://github.com/sonnyrd",
        'About': "# Vegetable Image Classification"
    }
)

if 'pred' not in st.session_state:
	st.session_state.pred = 0

# Load the model
model = tf.keras.models.load_model("model_best_improvement.hdf5")

# Initialize img variable
img = None

# Load image function
def load_image_inf(img):
    x = np.array(img)
    x = tf.image.resize_with_pad(x, 128, 128)
    x = tf.cast(x,tf.float32)/255.
    return x

# image Class
image_class = {'Bean': 0,
 'Bitter Gourd': 1,
 'Bottle Gourd': 2,
 'Brinjal': 3,
 'Broccoli': 4,
 'Cabbage': 5,
 'Capsicum': 6,
 'Carrot': 7,
 'Cauliflower': 8,
 'Cucumber': 9,
 'Papaya': 10,
 'Potato': 11,
 'Pumpkin': 12,
 'Radish': 13,
 'Tomato': 14}

# Predict function
def predict_image(img):
    inf = load_image_inf(img) 
    res = model.predict(x=np.expand_dims(inf, axis=0))
    res = np.argmax(res,axis=1)
    res = res.item()
    inv_map = {v: k for k, v in image_class.items()}
    title = inv_map[res]
    return title

# def change image
def change_image():
    st.session_state.pred = 0

# image header 
st.image('https://rosemaryacre.com.au/wp-content/uploads/2019/09/cropped-vegetable-header-3.jpg',use_column_width=True)

# Header Section
st.markdown(
    "<h1 style='text-align: center'>🥦 Vegetable Classification 🥦</h1>",
    unsafe_allow_html=True,
)

# Image Upload Option
choose = st.selectbox("Choose an option", ["Upload Image", "From URL"],on_change=change_image)

if choose == "Upload Image":  
    file = st.file_uploader("Choose an image...", type=["jpg","jpeg"])
    if file is not None:
        img = Image.open(file)


else:  
    url = st.text_area("Enter URL", placeholder="Paste the image URL here...")
    if url:
        try: 
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))
        except:  
            st.error(
                "Invalid URL!!!! Please use a different URL or upload an image."
            )


# check if image not none
if img is not None:
    col1, col2, col3  = st.columns([1,0.15,1])
    with col2:
        if st.button("Predict"):
            st.session_state.pred = 1


# Prediction Section
if st.session_state.pred == 1 and img is not None:
    col4, col5, col6 = st.columns([1, 3, 1])
    with col5:
        title = f"<h2 style='text-align:center'>{(predict_image(img))}</h2>"
        st.markdown(title, unsafe_allow_html=True)    
        st.image(img, use_column_width=True)

        st.write('is the prediction correct?')
        if st.button("Yes"):
           st.write("Yeaaaay!!")
           link_name = str(predict_image(img))
           link_name = link_name.replace(" ", "+")
           link = f"[Here](https://en.wikipedia.org/w/index.php?search={str(link_name)})"
           
           st.markdown(f'Click {link} if you want to know more about this vegetable', unsafe_allow_html=True)
        if st.button("Not Sure"):
            st.write('We are sorry to hear that!')
