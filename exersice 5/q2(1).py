def clean_text(text):
    """Remove unnecessary characters from the text."""
    return text.replace('.', '').replace('،', '').replace(':', '')

def find_similar_words(n, sentence, word):
    """Find similar words in the sentence."""
    sentence = clean_text(sentence)
    words = sentence.split()

    similar_words = []
    for candidate_word in words:
        distance = sum(c1 != c2 for c1, c2 in zip(candidate_word, word))
        
        if len(candidate_word) != len(word):
            distance += abs(len(candidate_word) - len(word))
            
        if distance <= n:
            similar_words.append(candidate_word)

    return similar_words

def main():
    n = int(input("Enter the value of n: "))
    sentence = input("Enter the sentence: ")
    word = input("Enter the word to compare: ")

    result = find_similar_words(n, sentence, word)

    for similar_word in result:
        print(similar_word)

if __name__ == "__main__":
    main()
