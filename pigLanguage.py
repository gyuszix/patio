def pig_it(text):
    text_list = text.split()
    empty_list = []
    for word in text_list:
        if word == "!" or word == '?':
            empty_list.append(word)
        else:
            new_word = word[1:] + word[0] + 'ay'
            empty_list.append(new_word)

    pig_words = " ".join(empty_list)

    return pig_words


text = "Pig latin is cool !"

print(pig_it(text))
