sentence = input("Write a sentence: ")
sentence_Dict = {}
for i in sentence:
    if i in sentence_Dict:
        sentence_Dict[i] += 1
    else:
        sentence_Dict[i] = 1
                                       
print(sentence_Dict)
