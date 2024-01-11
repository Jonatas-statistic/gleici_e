from googletrans import Translator

def translate_to_en(text: str):
    translator = Translator()
    translation = translator.translate(text, src='auto', dest='en')
    return translation.text