import spacy

nlp = spacy.load("en_core_web_sm")
sentence = input("Type a sentence (enter to use preset): ")
if sentence == "":
    sentence = "The quick brown fox jumps over the lazy dog."

doc = nlp(sentence)

print("Word\tPOS\n")
for token in doc:
    print(f"{token.text}\t{token.pos_}")
