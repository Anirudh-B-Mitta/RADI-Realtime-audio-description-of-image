import streamlit as st
from PIL import Image
from helper_fcns import story, audio_maker, translator

logo = Image.open("res/logo_V2.png")

st.set_page_config(
    page_title= "Story Teller",
    page_icon= logo
)

st.image(Image.open("res/logo_V1.png"), width=75)
st.markdown("# 🤡 Story Teller")
st.sidebar.markdown("# Story Teller")

st.write("\n")
uploaded_image = st.file_uploader("Upload an Image to imagine a story on:",type=["jpeg", "png", "jpg"])
lang = st.selectbox("Language: ",['English', 'Kannada', 'Hindi', 'Telugu', 'Urdu'])

if uploaded_image != None:
    if st.button("Submit"):
        try:
            uploaded_image = Image.open(uploaded_image)
            uploaded_image.save("res/temp.png")
            st.image(uploaded_image, width=200)
            text = story.story_tell()
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
    st.image(Image.open("res/Str_Tlr.png"))
    st.markdown("##### Hear Article")
    st.audio("res/Str_Tlr.mp3")
    st.markdown("##### Read Article")
    st.write('''Let's break down the function step by step:

Accepting an Image: The function takes an image as input. This can be either the image file path or the image data itself, depending on how the function is designed.

Image Captioning: The function utilizes an image captioning model to generate a textual description or caption for the given image. Image captioning models combine computer vision techniques with natural language processing to analyze the content of an image and generate a relevant caption that describes it.

Captioning the Image: Once the image captioning model has processed the image, it generates a caption that describes the contents or scene depicted in the image. This caption serves as a textual representation of the image.

Fictional Story Generation: After obtaining the caption, the function uses it as a prompt to an NLP (Natural Language Processing) model, which is capable of generating fictional stories. The NLP model takes the caption as input and generates a fictional story related to the content described in the caption. The NLP model uses its language generation capabilities to create a coherent and imaginative story.

Output: The final output of the function is the generated fictional story, which can be returned as a string or displayed in a desired format.

Overall, this function combines computer vision techniques, image captioning, and natural language processing to create a process where an image is first captioned, and then a fictional story is generated based on that caption. It's an interesting combination of image understanding and creative text generation, allowing for the creation of imaginative narratives based on visual content.''')