def popular_words(text, words):

    text = text.lower()

    text_words = text.split()


    result = {word: 0 for word in words}


    for word in words:
        result[word] = text_words.count(word)

    return result



text = '''When I was One I had just begun
When I was Two I was nearly new'''
words = ['i', 'was', 'three', 'near']

print(popular_words(text, words))  # {'i': 4, 'was': 3, 'three': 0, 'near': 0}