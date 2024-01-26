n = int(input())
sentence = input()
sentence = sentence.replace('.', '')
sentence = sentence.replace('،', '')
sentence = sentence.replace(':', '')
word = input()
def find_similar_words(n, sentence, word):
    words = sentence.split()
    similar_words = []
    for i in words:
        distance = sum(c1 != c2 for c1, c2 in zip(i, word))
        if len(i) != len(word):
         distance += abs(len(i) - len(word))
        if distance <= n:
            similar_words.append(i)
    return similar_words

result = find_similar_words(n, sentence, word)
for i in range (len(result)):
    print(result[i])



