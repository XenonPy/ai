import spacy

nlp = spacy.load("en_core_web_sm")
sentence = input("Enter the sentence for named entities to be detected (enter for preset): ")
if not sentence:
    sentence = "Apple is looking at buying U.K. startup for $1 billion"
doc = nlp(sentence)

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)