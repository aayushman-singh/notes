def terms(text):
    return {word.strip('.,:;!?()[]').lower() for word in text.split() if len(word) > 3}
