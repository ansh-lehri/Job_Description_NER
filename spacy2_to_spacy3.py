from spacy.tokens import DocBin
import spacy
import json
from tqdm import tqdm
import random

def load_data(file):
    print("YYY")
    with open(file,'r',encoding="utf-8") as f:
        data = json.load(f)
    return(data)
    

intern_train = load_data(b"C:\Users\Dell\Desktop\job collector\Job\data\ubiai_data_validation.json")
print(intern_train)

nlp = spacy.blank("en")
def create_training(TRAIN_DATA):

    db = DocBin()
    for text,annot in tqdm(TRAIN_DATA):
        doc=nlp.make_doc(text)
        ents=[]
        for start,end,label in annot['entities']:
            span = doc.char_span(start,end,label=label,alignment_mode="contract")
            if span is None:
                print("Skipping entity")
            else:
                ents.append(span)
        doc.ents=ents
        db.add(doc)
    return db
    
intern_train = create_training(intern_train)
intern_train.to_disk("C://Users//Dell//Desktop//job collector//Job//data//ubiai_data_validation.spacy")