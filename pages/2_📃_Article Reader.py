import streamlit as st
from PIL import Image
from helper_fcns import ocr, audio_maker, translator

logo = Image.open("res/logo_V2.png")

st.set_page_config(
    page_title= "Article Reader",
    page_icon= logo
)

st.image(Image.open("res/logo_V1.png"), width=75)
st.markdown("# 📃 Article Reader")
st.sidebar.markdown("# Article Reader")

st.write("\n")
uploaded_image = st.file_uploader("Upload an Article (only English):",type=["jpeg", "png", "jpg"])
lang = st.selectbox("Translate to (if required): ",['English', 'Kannada', 'Hindi', 'Telugu', 'Urdu'])

if uploaded_image != None:
    if st.button("Submit"):
        try:
            uploaded_image = Image.open(uploaded_image)
            uploaded_image.save("res/temp.png")
            st.image(uploaded_image, width=200)
            text = ocr.read_img()
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
    st.image(Image.open("res/OCR.png"))
    st.markdown("##### Hear Article")
    st.audio("res/OCR.mp3")
    st.markdown("##### Read Article")
    st.write('''OCR, or optical character recognition, is a technology that can identify text in images. It works by first converting the image into a black-and-white bitmap. Then, the OCR software analyzes the bitmap to identify individual characters. This is done by comparing the bitmap to a database of known character patterns. Once the characters have been identified, they are converted back into text.

The model of ocr.space works in a similar way, but it uses a neural network to identify characters. Neural networks are a type of machine learning algorithm that can learn to recognize patterns. In the case of ocr.space, the neural network is trained on a large dataset of images of text. This allows the neural network to learn to identify characters even if they are distorted or in poor quality.

The specific steps that ocr.space takes to identify text are as follows:

The image is converted into a black-and-white bitmap.
The bitmap is segmented into individual characters.
Each character is represented as a vector of features.
The vector of features for each character is passed to the neural network.
The neural network outputs a probability distribution over all possible characters.
The character with the highest probability is selected as the identified character.
The accuracy of ocr.space depends on the quality of the image and the size of the training dataset. In general, ocr.space is able to achieve high accuracy, even on images that are distorted or in poor quality.

Here are some additional details about how ocr.space works:

The neural network that ocr.space uses is a deep learning model called a convolutional neural network (CNN). CNNs are a type of neural network that are specifically designed for image recognition.
The training dataset for ocr.space is a large collection of images of text. The images in the training dataset are drawn from a variety of sources, including books, magazines, newspapers, and websites.
The accuracy of ocr.space is constantly being improved. The developers of ocr.space are constantly adding new data to the training dataset and improving the neural network.
Overall, ocr.space is a powerful OCR tool that can be used to identify text in images. It is accurate, reliable, and easy to use.''')