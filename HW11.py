def count_words(sentences):
    word_counts = []
    for sentence in sentences.split('.'):
        if sentence:
            word_count = 0
            for char in sentence.split():
                if char:
                    word_count += 1
            word_counts.append(word_count)
    return word_counts

sentences = input("Please write sentences: ")
words_number = count_words(sentences)
print(words_number)