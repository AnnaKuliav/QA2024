from colorama import *
sentences = input(Fore.CYAN +"Please write sentences: ")
words = sentences.split()

result_words = []

for word in words:
    if 'oo' in word.lower():
        result_words.append(word.capitalize())

print(Fore.BLUE + "Results:", ' '.join(result_words))