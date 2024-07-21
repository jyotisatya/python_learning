def clean_item(item):
    clean_word = ""
    for char in item:
        if char.isalnum():
            clean_word += char
    return clean_word
