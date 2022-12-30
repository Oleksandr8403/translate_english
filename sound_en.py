from gtts import gTTS
import os

text_for_translate = []

# name_file_for_translate_txt = input("Enter name of txt file (without .txt, only name): ")
name_file_for_translate_txt = 'aboutme'

path_to_project = os.getcwd()
path_to_words_file = os.path.join(path_to_project, "for_translate", name_file_for_translate_txt + '.txt')
path_to_translated_file_mp3 = os.path.join(path_to_project, "translated_mp3",
                                           name_file_for_translate_txt + '_sound.mp3')

with open(path_to_words_file, 'r') as file1:
    for item in file1:
        text_for_translate.append(item)
print(text_for_translate)

with open(path_to_translated_file_mp3, 'wb') as fp:
    for i in text_for_translate:
        my_obj = gTTS(text=i[:-1], lang='en', slow=False)
        my_obj.write_to_fp(fp)
        print(i[:-1])



