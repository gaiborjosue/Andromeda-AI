from googletrans import Translator

sentence = str(input("Type in the command prompt the sentence or word you want to translate....  "))

translator=Translator()

translated_sentence = translator.translate(sentence, src='es', dest='en')

print(translated_sentence.text)