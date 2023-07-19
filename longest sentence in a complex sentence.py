sentences="My name is Eve,I come from chennai,India,I am here for research work."
length = sentences.split(",") or sentences.split(".")
tokenized_sentences = [sentence.split(" ") for sentence in length]
longest_sen = max(tokenized_sentences, key=len)
longest_sen_length = len(longest_sen)
print("The longest sentence has", (longest_sen_length), "words.")
print("The longest sentence is : ", " ".join(longest_sen))
