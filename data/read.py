import os
import json


def save_data(file, data):

    with open(file, 'w', encoding="utf-8") as f:
        json.dump(data, f, indent=4)


annotate_data = []
files = os.listdir("C://Users//Dell//Desktop//Job Data//train")

for file in files:

    file_path = "C://Users//Dell//Desktop//Job Data//train" + "//" + file

    annotations = open(file_path,'r',encoding="utf-8")
    labels = annotations.read()
    annotations.close()
    
    labels = eval(labels)
    print(labels)
    try:
        annotate_data.append(labels[0])
    except:
        print("NOT POSSIBLE")

print(annotate_data)

save_data("C://Users//Dell//Desktop//Job Data//ubiai_data.json", annotate_data)

