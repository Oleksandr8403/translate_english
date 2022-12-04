from gtts import gTTS
from googletrans import Translator
from fpdf import FPDF

translator = Translator()
text_for_translate = []
dict_for_pdf = []

pdf = FPDF()
pdf.add_page()
pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
pdf.set_font('DejaVu', '', 18)

with open('words_for_translate.txt_2', 'r') as file1:
    for item in file1:
        text_for_translate.append(item)

with open("translate_2.txt", "w") as file2:
    pass

k = 1
with open("translate_2.txt", "a") as file3:
    for word in text_for_translate:
        result_ru = translator.translate(word, dest='ru')
        translate_text_ru = result_ru.text
        full_text = word[:-1].upper() + '\n' + translate_text_ru + '\n'
        text_pdf = word[:-1] + '  -  ' + translate_text_ru
        pdf.cell(200, 12, txt=text_pdf, ln=k, align='C')
        print('written word number = ', k)
        k += 1
        file3.write(full_text)

pdf.output("translate_2.pdf")

my_text = ''
my_text1 = ''
dict_words = []

with open('translate_2.txt', 'r') as file:
    for item in file:
        dict_words.append(item)
with open('translate_audio_2.mp3', 'wb') as fp:
    # need test range(len(dict_words)+1) because in mp3 file is absent last word from words_for_translate.txt
    for i in range(len(dict_words)):
        if i % 2 == 0:
            my_obj = gTTS(text=dict_words[i], lang='en', slow=True)
            my_obj.write_to_fp(fp)
            print('written sound number = ', i)
        else:
            my_obj1 = gTTS(text=dict_words[i], lang='ru', slow=True)
            my_obj1.write_to_fp(fp)
            print('written sound number = ', i)
