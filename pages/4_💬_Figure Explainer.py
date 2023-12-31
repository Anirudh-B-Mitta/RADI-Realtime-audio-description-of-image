import streamlit as st
from PIL import Image
from helper_fcns import fig_exp, audio_maker, translator

logo = Image.open("res/logo_V2.png")

st.set_page_config(
    page_title= "Figure Explainer",
    page_icon= logo
)

st.image(Image.open("res/logo_V1.png"), width=75)
st.markdown("# 💬 Figure Explainer")
st.sidebar.markdown("# Figure Explainer")

st.write("\n")
uploaded_image = st.file_uploader("Upload an Image from textbook:",type=["jpeg", "png", "jpg"])
class_chosen = st.selectbox("Class: ",["Select",1,2,3,4,5,6,7,8,9,10,11,12])
hint = st.text_input("Hint for the Image (The topic/Image Name):")
lang = st.selectbox("Language: ",['English', 'Kannada', 'Hindi', 'Telugu', 'Urdu'])

if uploaded_image != None and class_chosen != "Select" and len(hint.strip()):
    if st.button("Submit"):
        try:
            uploaded_image = Image.open(uploaded_image)
            uploaded_image.save("res/temp.png")
            st.image(uploaded_image, width=200)
            text = fig_exp.explain_fig(class_chosen, hint)
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
    st.image(Image.open("res/Fig_Exp.png"))
    st.markdown("##### Hear Article")
    st.audio("res/Fig_Exp.mp3")
    st.markdown("##### Read Article")
    st.write('''Here's a breakdown of how this function works:

Input: The function takes an image from a textbook as input. This image could be in a file format like JPEG or PNG.

Image Captioning: The image is passed through an image captioning model. The image captioning model is trained to analyze the visual features of an image and generate a textual description or caption that represents the content of the image. This model generates a caption for the input image.

Caption to Question: The generated caption from the image captioning model is then used as a question for an NLP model. This NLP model is designed to take a question as input and provide an explanation or answer based on the question.

NLP Model: The NLP model receives the caption as a question and processes it. This model is trained on a large dataset of questions and answers or explanations. It understands the context of the question and generates a response that explains the figure depicted in the image. The NLP model may use techniques such as natural language understanding, text generation, or machine comprehension to generate the explanation.

Output: Finally, the function returns the explanation generated by the NLP model as the output.

Overall, this function combines the capabilities of an image captioning model and an NLP model to provide an explanation of the figure in the input image. It uses the image captioning model to generate a question about the image and then utilizes the NLP model to generate an explanation based on that question.''')