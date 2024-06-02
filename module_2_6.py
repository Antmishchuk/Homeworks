def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        if root_word.lower() in str(word).lower():
            same_words.append(word)
        elif str(word).lower() in root_word.lower():
            same_words.append(word)
    print(*same_words)
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')