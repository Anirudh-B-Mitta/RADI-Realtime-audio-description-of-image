import streamlit as st
from PIL import Image
from helper_fcns import count_object, translator, audio_maker

logo = Image.open("res/logo_V2.png")

st.set_page_config(
    page_title= "Object Counter",
    page_icon= logo
)

st.image(Image.open("res/logo_V1.png"), width=75)
st.markdown("# 🔢 Object Counter")
st.sidebar.markdown("# Object Counter")

st.write("\n")
uploaded_image = st.file_uploader("Upload an Image to count:",type=["jpeg", "png", "jpg"])
lang = st.selectbox("Language: ",['English', 'Kannada', 'Hindi', 'Telugu', 'Urdu'])

if uploaded_image != None:
    if st.button("Submit"):
        try:
            uploaded_image = Image.open(uploaded_image)
            uploaded_image.save("res/temp.png")
            st.image(uploaded_image, width=200)
            text = count_object.counting()
            if(lang == 'English'):
                audio_maker.make_aud(text,'en')
            elif(lang == 'Kannada'):
                text = translator.translator(text,'kn')
                audio_maker.make_aud(text,'kn')
            elif(lang == 'Hindi'):
                text = translator.translator(text,'hi')
                audio_maker.make_aud(text,'hi')
            elif(lang == 'Telugu'):
                text = translator.translator(text,'te')
                audio_maker.make_aud(text,'te')
            elif(lang == 'Urdu'):
                text = translator.translator(text,'ur')
                audio_maker.make_aud(text,'ur')
            st.audio("res/temp.mp3")
            st.write(text)
        except:
            st.write("Something went wrong. Try again")

st.write("\n")
if st.checkbox(" Read About Algorithm"):
    st.image(Image.open("res/Obj_Ctr.png"))
    st.markdown("##### Hear Article")
    st.audio("res/Obj_Ctr.mp3")
    st.markdown("##### Read Article")
    st.write('''Object identification is the process of identifying objects in an image. This can be done by using a variety of techniques, including:

Feature matching: This technique involves comparing the features of an object in an image to a database of known features.
Object detection: This technique involves identifying the boundaries of an object in an image.
Classification: This technique involves assigning a label to an object in an image.
The cvlib library in Python is a machine learning library that can be used for object identification. The cvlib library includes a number of functions for object detection and classification.

One of the most popular functions in the cvlib library for object identification is the detect_common_objects() function. This function takes an image as input and returns a list of the objects that were detected in the image. The detect_common_objects() function uses a pre-trained model to detect objects in images. The pre-trained model is trained on a dataset of images that contain a variety of objects.

The cvlib library also includes a number of other functions for object identification. These functions allow you to customize the object detection process. For example, you can specify the confidence threshold for object detection. The confidence threshold is a value that determines how confident the cvlib library must be that an object has been detected before it is returned.

Object identification is a powerful technique that can be used for a variety of tasks. For example, object identification can be used to:

Identify objects in images for security purposes.
Identify objects in images for marketing purposes.
Identify objects in images for medical purposes.
The cvlib library is a powerful tool that can be used for object identification. The cvlib library is easy to use and it includes a number of functions for object detection and classification.''')