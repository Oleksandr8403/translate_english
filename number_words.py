# variables
our_string = ''
name_input_file = '22222.txt'
name_output_file = 'words_count1.txt'
k = 0
temp_list_words = our_string.split(" ")
list_symbols = [';', ':', '+', '-', '!', '&', '?', '*', ' ', '', ',', '.', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                '0', '\n', '"']
final_word_list = []
final_dict = {}
with open(name_input_file, 'r') as file1:
    for item in file1:
        our_string += ' ' + item
for word1 in temp_list_words:
    for symbol in list_symbols:
        if symbol in word1:
            word1 = word1.strip(symbol)
    temp_list_words[k] = word1.lower()
    k += 1
for word2 in temp_list_words:
    if word2 not in list_symbols:
        final_word_list.append(word2)
for word3 in final_word_list:
    final_dict[word3] = final_word_list.count(word3)
final = sorted(final_dict.items(), key=lambda x: x[1], reverse=True)
print(final)
with open(name_output_file, "w") as file2:
    for tuple1 in final:
        file2.write(str(tuple1[0]) + ' - ' + str(tuple1[1]) + '\n')
