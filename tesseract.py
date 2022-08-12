from PIL import Image
import pytesseract
import os
import cv2
import pytesseract
import numpy as np
from PIL import Image
from io import BytesIO
import pandas as pd
import glob
import csv
import re


# folder path
dir_path = r'/home/chathushkavi/projects/tesseract/images'
parent_path = r'/home/chathushkavi/projects/tesseract' 

directory = "corpus"

csv_path = os.path.join(parent_path, directory)

if not os.path.exists(csv_path):
    os.mkdir(csv_path)
    
texts =[]

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):

        im = Image.open(path)
        text = pytesseract.image_to_string(im, lang="tam+eng")
        new_text = text.replace("\n", " ")

        with open(csv_path + '/corpus.csv', 'a') as fp:
            sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', new_text)
            for sent in sentences:
                fp.write("%s " % sent)
                fp.write('\n')




# from PIL import Image
# import pytesseract
# import os
# import cv2
# import pytesseract
# import numpy as np
# from PIL import Image
# from io import BytesIO
# import pandas as pd
# import glob
# import csv
# import re


# # folder path
# dir_path = r'/home/chathushkavi/projects/tesseract/images'
# parent_path = r'/home/chathushkavi/projects/tesseract' 

# directory = "corpus"

# csv_path = os.path.join(parent_path, directory)

# if not os.path.exists(csv_path):
#     os.mkdir(csv_path)
    
# texts =[]

# # Iterate directory
# for path in os.listdir(dir_path):
#     # check if current path is a file
#     if os.path.isfile(os.path.join(dir_path, path)):

#         im = Image.open(path)
#         text = pytesseract.image_to_string(im, lang="tam+eng")
#         new_text = text.replace("\n", " ")
#         sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', new_text)
#         for sent in sentences:
#             texts.append(sent)
#             df=pd.DataFrame(texts)

# df.to_csv('/home/chathushkavi/projects/tesseract/corpus/corpus.csv', index=False)


# # import the necessary packages
# import pytesseract
# import argparse
# import cv2
# # construct the argument parser and parse the arguments}
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
# 	help="path to input image to be OCR'd")
# args = vars(ap.parse_args())

# # load the input image and convert it from BGR to RGB channel
# # ordering}
# image = cv2.imread(args["image"])
# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# # use Tesseract to OCR the image
# text = pytesseract.image_to_string(image, lang="tam+eng")

# with open('skandha' + '.txt', 'w') as fp:
#     fp.write("%s" % text)
    
# print(text)