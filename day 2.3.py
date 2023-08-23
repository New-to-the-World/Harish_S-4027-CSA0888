def max_words_in_sentence(sentences):
    max_words = 0   
    for sentence in sentences:
        words = sentence.split()  
        max_words = max(max_words, len(words))  
    return max_words

num_sentences = int(input("Enter the number of sentences: "))
sentences = []
for _ in range(num_sentences):
    sentence = input("Enter a sentence: ")
    sentences.append(sentence)
result = max_words_in_sentence(sentences)
print("The maximum number of words in a single sentence is:", result)
