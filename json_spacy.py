import json

def load_data(path):
    with open(path,'r',encoding="utf-8") as f:
        data = json.load(f)
    return data
    
    
def save_data(path,data):
    with open(path,'w',encoding="utf-8") as f:
        json.dump(data,f,indent=4)
        
        
data = load_data("C://Users//Dell//Desktop//job collector//job//data//indeed_geeks_test.json")

entities = data['_views']['_InitialView']['NamedEntity']

sentence_ranges = data['_views']['_InitialView']['Sentence']

real_text = data['_referenced_fss']['1']['sofaString'].split('\r\n')

print(len(sentence_ranges))
print(len(real_text))

start = 1
end=0
j=1
check = []
for i in real_text:

    #print("***********************")
    '''
    if j==1:
        x=i 
        j=0
    else:
        x = "  "+i
    '''
    end+=len(i)
    #print(start,"    ,    ",end)
    check.append({"start":start,"end":end})
    start=end+2
    end=end+2

sentence_ranges[0].update({"begin":1})

'''
for i in range(len(sentence_ranges)):

    if sentence_ranges[i]['begin']!=check[i]['start'] or sentence_ranges[i]['end']!=check[i]['end']:
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print()
        print(i)
        print("Sentence Ranges    ", sentence_ranges[i]['begin'],"      ,      ",sentence_ranges[i]['end'])
        print("Check Ranges       ", check[i]['start'],"      ,     ",check[i]['end'])

'''
new_sentence_ranges = []

si=0
ci=0

print(sentence_ranges[0]["begin"],"    ",sentence_ranges[0]['end'])

while si<len(sentence_ranges) and ci<len(check):

    if sentence_ranges[si]["begin"]==check[ci]['start'] and sentence_ranges[si]['end']==check[ci]['end']:
        new_sentence_ranges.append({"sofa":1,"start":sentence_ranges[si]["begin"],"end":sentence_ranges[si]["end"]})
        si+=1
        ci+=1
    elif sentence_ranges[si]['begin']!=check[ci]['start'] or sentence_ranges[si]['end']!=check[ci]['end']:
        start_ind = min(sentence_ranges[si]['begin'],check[ci]['start'])
        end_ind = max(sentence_ranges[si]['end'],check[ci]['end'])

        if end_ind==sentence_ranges[si]['end'] and end_ind==check[ci]['end']:
            new_sentence_ranges.append({"sofa":1,"start":start_ind,"end":end_ind})
            ci+=1
        si+=1

while ci<len(check):
    new_sentence_ranges.append({"sofa":1,"start":check[ci]['start'],"end":check[ci]['end']})
    ci+=1


print(len(new_sentence_ranges))
print(len(real_text))
print(len(entities))

TRAIN_DATA = []
ei=0
si=0
entity = {"entities":[]}


for i in range(len(entities)):

    c=list(entities[i].keys())
    if 'value' in c:
        continue
    #print(i)
    entities[i].update({'value':'Technical_Skill'})

entity = {"entities":[]}
while si<len(new_sentence_ranges) and ei<len(entities):
    if new_sentence_ranges[si]['end']<entities[ei]['begin'] or new_sentence_ranges[si]['start']>entities[ei]['end']:
        print("TTTRRRUUUEEEEE")
        TRAIN_DATA.append([real_text[si],entity])
        entity = {"entities":[]}
        si+=1
    elif new_sentence_ranges[si]['start']<=entities[ei]['begin'] and new_sentence_ranges[si]['end']>=entities[ei]['end']:
        print("FFFFAAAAALLLLLLSSSSSEEEEE")
        entity['entities'].append([entities[ei]['begin'],entities[ei]['end'],entities[ei]['value']])
        if new_sentence_ranges[si]['end']==entities[ei]['end']:
            TRAIN_DATA.append([real_text[si],entity])
            entity = {"entities":[]}
            si+=1
        ei+=1

entity = {"entities":[]}
while si<len(new_sentence_ranges):
    TRAIN_DATA.append([real_text[si],entity])
    si+=1
    
print(TRAIN_DATA[4])
save_data("C://Users//Dell//Desktop//job collector//job//data//indeed_geeks_spacy_test.json",TRAIN_DATA)


