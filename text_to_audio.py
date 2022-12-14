from gtts import gTTS
from googletrans import Translator
from fpdf import FPDF
import os

translator = Translator()
text_for_translate = []
dict_for_pdf = []


name_file_for_translate_txt = input("Enter name of txt file with list words to translate (without .txt, only name): ")
print('Program will automatically create txt file with translated words.')
create_pdf_file = input("Do you need pdf file with translate? y/n? ").lower()
create_mp3_mp3 = input("Do you need mp3 file with translate? y/n? ").lower()

path_to_project = os.getcwd()
path_to_words_file = os.path.join(path_to_project, "for_translate", name_file_for_translate_txt + '.txt')
path_to_translated_file = os.path.join(path_to_project, "translated_txt", name_file_for_translate_txt + '_translated.txt')
path_to_translated_file_pdf = os.path.join(path_to_project, "translated_pdf", name_file_for_translate_txt + '_translated.pdf')
path_to_translated_file_mp3 = os.path.join(path_to_project, "translated_mp3", name_file_for_translate_txt + '_translated.mp3')

font_file_path = os.path.join(path_to_project, "font", "DejaVuSansCondensed.ttf")
pdf = FPDF()
pdf.add_page()
pdf.add_font('DejaVu', '', font_file_path, uni=True)
pdf.set_font('DejaVu', '', 18)

with open(path_to_words_file, 'r') as file1:
    for item in file1:
        text_for_translate.append(item)

with open(path_to_translated_file, "w") as file2:
    pass

k = 1
with open(path_to_translated_file, "a") as file3:
    for word in text_for_translate:
        result_ru = translator.translate(word, dest='ru')
        translate_text_ru = result_ru.text
        full_text = word[:-1].upper() + '\n' + translate_text_ru + '\n'
        if create_pdf_file == 'y':
            text_pdf = word[:-1] + '  -  ' + translate_text_ru
            pdf.cell(200, 12, txt=text_pdf, ln=k, align='C')
        print('written word number = ', k)
        k += 1
        file3.write(full_text)
if create_pdf_file == 'y':
    pdf.output(path_to_translated_file_pdf)

my_text = ''
my_text1 = ''
dict_words = []

if create_mp3_mp3 == 'y':
    with open(path_to_translated_file, 'r') as file:
        for item in file:
            dict_words.append(item)
    with open(path_to_translated_file_mp3, 'wb') as fp:
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

print('\ntxt file was created')
if create_pdf_file == 'y':
    print('pdf file was created')
if create_mp3_mp3 == 'y':
    print('mp3 file was created')
