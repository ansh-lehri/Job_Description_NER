import os
import zipfile

annotate_data = []
files = os.listdir("C://Users//Dell//Desktop//UBIAI downloads//relations_validation")

print(files)
for i in range(0,len(files)-1):

    path = "C://Users//Dell//Desktop//UBIAI downloads//relations_validation//" + files[i]

    with zipfile.ZipFile(path, 'r') as zip_ref:
        zip_ref.extractall("C://Users//Dell//Desktop//Job Data//relations_valid")