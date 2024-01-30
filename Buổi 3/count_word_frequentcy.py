word = ['apple','orange','banana','apple','orange','apple']
def count_word_frequency(word_list:list):
    frequency_dictionary = {}
    for elem in word_list:
        # Nếu dictionary chưa có gì thì thêm vào giá trị đầu tiên
        if len(frequency_dictionary) == 0:
            frequency_dictionary.update({elem:1})
        # Sau khi từ điển có 1 phần tử thì chạy bước này
        else:
            # Biến kiểm tra xem giá trị đã tồn tại hay chưa trong từ điển
            exists = False
            for key, value in frequency_dictionary.items():
                if elem == key:
                    # Nếu đã tồn tại thì sẽ cộng thêm giá trị vào phần tử
                    exists = True
                    frequency_dictionary[key]+=1
                    break
            # Nếu chưa tồn tại sẽ thêm vào tử điển với giá trị bằng 1
            if exists == False:
                frequency_dictionary.update({elem:1})
    return frequency_dictionary
dic = count_word_frequency(word)
print(dic)
