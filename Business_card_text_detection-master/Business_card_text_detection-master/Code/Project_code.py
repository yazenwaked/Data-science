import cv2
import pytesseract
import re


# loading the image
File_path = "../Images/IMG_0422.JPG"

# read the image
img = cv2.imread(File_path, -1)

# Image pre-processing

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, th_1 = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV) # for black backgrounds - binary - global
_, th_2 = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY) # for white backgrounds - binary - global

# detect the text in the image

text_1 = pytesseract.image_to_string(th_1)
text_2 = pytesseract.image_to_string(th_2)

length_1 = len(text_1)
length_2 = len(text_2)

if length_1 > length_2:
    text_image = text_1
else:
    text_image = text_2

# Test processing

text_lst = text_image.splitlines() # This is to get each line as a seperate text
text_lst = [word for word in text_lst if len(word)!= 0]

def get_full_name(lst):
    for idx in lst:
        full_name = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", idx)
        if full_name is not None:
            return idx

def get_email(lst):
    for idx in lst:
        mail = re.search(r'[\w\.-]+@[\w\.-]+', idx)
        if mail is not None:
            return idx

def get_phone_number(lst):
    for idx in lst:
        for i in range(0, len(idx)):
            if idx[i][0] == "+":
                return idx
            elif idx[i][0] == "0":
                return idx




Name = ""
Telephone = ""
Email = ""
#===========
Final_text = {"Name": get_full_name(text_lst),
              "Telephone" : get_phone_number(text_lst),
              "Email" : get_email(text_lst),}

print(Final_text)
