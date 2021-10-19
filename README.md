# Job_Description_NER

This project was developed to analyse job descriptions on various platforms and identify entities like technical skills, soft skills, experience, salary etc.
Job descriptions from Indeed, Internshala and GeeksGod were used in developing the NER. 
Used UBIAI Data Annotation Tool for data annotation.
Used spacy transformers to develop the model.


Contents of the repo:

1. data folder: Contains .json and .spacy files of data. .json files contain annotated data exported from UBIAI tool. .spacy files contain .json data converted into spacy format.
2. base_config.cfg: This is the basic spacy configuration file needed for spacy custom ner training. Contents of this file are copied from spacy website. 
                    This file contains path to training, test and validation data. Later on, this file is converted into config.cfg using terminal commands which contains extra parameters
                    added by spacy itself.
                    
3. json_spacy.py: This file contans code to convert annotated data in json format to standard spacy format.
4. spacy2_to_spacy3.py: This contains code to convert data in spacy2 format(obtained from json_spacy.py) to spacy3 format.

5. Transformer_ner.ipynb: This workbook contains code for converting base_config.cfg to config.cfg and for training the model.


Link to trained model: https://bit.ly/3G3UJAy
