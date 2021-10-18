import json


def save_data(file, data):

    with open(file, 'w', encoding="utf-8") as f:
        json.dump(data, f, indent=4)


# Read output json file from WebAnno (Annotation tool)
with open('C://Users//Dell//Desktop//job collector//job//data//indeed_geeks_train.json','r',encoding='utf-8') as data_file:    
    data = json.load(data_file)

# Extract original sentences
sentences_lists = data['_referenced_fss']['1']['sofaString'].split('\r\n')
#print(len(sentences_lists))

a = [j for j in sentences_lists if j!='']

#print(len(a))


c=''''about the company milestone infosoft solutions private limited is a global but mumbai based software company established in the year 2005 and providing customer centric and customer specific software solutions.'''
print(len(c))

sentences = ""

for i in sentences_lists:
    i+="."
    sentences+=i

sentences_list = sentences.split('.')
#print(len(sentences_list))
# Extract entity start/ end positions and names
ent_loc = data['_views']['_InitialView']['NamedEntity']

# Extract Sentence start/ end positions
Sentence = data['_views']['_InitialView']['Sentence']
#print(ent_loc[254])
# Set first sentence starting position 0
Sentence[0]['begin'] = 0

# Prepare spacy formatted training data

for i in range(len(ent_loc)):

    c=list(ent_loc[i].keys())
    if 'value' in c:
        continue
    #print(i)
    ent_loc[i].update({'value':'Technical_Skill'})

#print(Sentence[92])
#print(ent_loc[92])

TRAIN_DATA = []
ent_list = []
for sl in range(0,len(Sentence)):
    ent_list_sen = []
    for el in range(0,len(ent_loc)):
        if(ent_loc[el]['begin'] >= Sentence[sl]['begin'] and ent_loc[el]['end'] <= Sentence[sl]['end']):
            ## Need to subtract entity location with sentence begining as webanno generate data by treating document as a whole
            #print()
            #print(sl,"    ",el)
            ent_list_sen.append([(ent_loc[el]['begin']-Sentence[sl]['begin']),(ent_loc[el]['end']-Sentence[sl]['begin']),ent_loc[el]['value']])
    ent_list.append(ent_list_sen)
    ## Create blank dictionary
    ent_dic = {}
    ## Fill value to the dictionary
    ent_dic['entities'] = ent_list[-1]
    ## Prepare final training data
    #print(sl,ent_dic)
    print(sl, " ", [sentences_list[sl],ent_dic])
    TRAIN_DATA.append([sentences_list[sl],ent_dic])

print(TRAIN_DATA[0])
file = "C://Users//Dell//Desktop//job collector//job//data//indeed_geeks_spacy_train.json"
save_data(file,TRAIN_DATA)
