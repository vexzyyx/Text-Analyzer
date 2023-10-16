import re

def analyze_text(text):
    vowels = []
    consonants = []
    whitespaces = []
    numbers = []
    other_characters = []
    characters_count = len(text)
    uppercase_letters = 0
    lowercase_letters = 0
    words = text.split()
    sentences = re.split(r'[.!?]', text)
    common_words = ["to", "the", "of", "be", "and", "that", "how", "hello", "many", "good", "go", "went", "really", "have", "not", "with", "ready", "you", "from", "there", "he", "him", "she", "her"]

    for word in words:
        if word in common_words:
            is_english = True
            break
        else:
            is_english = False
    

    for char in text:
        if char.isupper():
            uppercase_letters += 1
        elif char.islower():
            lowercase_letters += 1
        if char in "aeiou":
            vowels.append(char)
        elif char.isalpha():
            consonants.append(char)
        elif char.isspace():
            whitespaces.append(char)
        elif char.isnumeric():
            numbers.append(char)
        else:
            other_characters.append(char)

    avg_wordlength = ((len(vowels) + len(consonants)) / len(words))

    sentence_lengths = []
    for sentence in sentences:
        sentence_lengths.append(len(sentence.split()))
    avg_words_in_sentence = sum(sentence_lengths) / len(sentence_lengths)

    print(f"Is English: {is_english}")
    print(f"Number of Characters (with spaces): {characters_count}")
    print(f"Letters: {len(vowels) + len(consonants)}")
    print(f"Uppercase Letters: {uppercase_letters}")
    print(f"Lowercase Letters: {lowercase_letters}")
    print(f"Number of Words: {len(words)}")
    print(f"Number of Sentences: {len(sentences)}")
    print(f"AVG Word Length: {avg_wordlength:.2f}")
    print(f"AVG Words in a Sentence: {avg_words_in_sentence:.2f}")
    print(f"Whitespaces: {len(whitespaces)}")
    print(f"Numbers: {len(numbers)}\n{numbers}")
    print(f"Other Characters: {len(other_characters)}\n{other_characters}")
    print(f"Vowels: {len(vowels)}\n{vowels}")
    print(f"Consonants: {len(consonants)}\n{consonants}")

text = input("Input your text to analyze: ")
analyze_text(text)
