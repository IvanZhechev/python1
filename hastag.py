import string


def generate_hashtag(text):
    clean_text = ''.join(char for char in text if char not in string.punctuation).replace(" ", "")

    words = clean_text.title()

    hashtag = f"#{words}"


    if len(hashtag) > 140:
        hashtag = hashtag[:140]

    return hashtag


print(generate_hashtag("Python Community"))  # => #PythonCommunity
print(generate_hashtag("i like python community!"))  # => #ILikePythonCommunity
print(generate_hashtag("Should, I. subscribe? Yes!"))  # => #ShouldISubscribeYes
