import requests

api_key = 'K81598583888957'

def read_img():
    image_path = "res/temp.png"
    image_data = open(image_path, 'rb').read()
    response = requests.post('https://api.ocr.space/parse/image',
                            files={'image': (image_path, image_data)},
                            data={'apikey': api_key, 'OCREngine': 2})
    data = response.json()
    print(data)
    text = data['ParsedResults'][0]['ParsedText']
    return text