import requests
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

def  describer():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large").to("cuda")

    img_url = 'res/temp.png'
    img = Image.open(img_url).convert('RGB')

    inputs = processor(img, return_tensors="pt").to("cuda")
    output = model.generate(**inputs)
    return(processor.decode(output[0],skip_special_tokens = True))