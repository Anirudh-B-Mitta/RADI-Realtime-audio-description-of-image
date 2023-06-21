from googletrans import Translator

def translator(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    translated_text = translation.text
    return translated_text