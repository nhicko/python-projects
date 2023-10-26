def reverse_words(sentence):
    words = sentence.split(" ")

    new_word_list = [word[::-1] for word in words]

    res_str = " ".join(new_word_list)
    return res_str


str1 = "My Name is Jessa"
print(reverse_words(str1))
