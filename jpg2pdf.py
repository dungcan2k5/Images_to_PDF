import os
import re
from PIL import Image

while True:
    # Regex to sort file name
    def atoi(text) :
        return int(text) if text.isdigit() else text
    def natural_keys(text) :
        return [ atoi(c) for c in re.split(r'(\d+)', text) ]

    # Guide
    print(r'''Enter the folder path containing the image files you want to convert to a PDF file.
    Example: C:\Users\Administrator\Desktop\
    Another way is to drag and drop the folder here.''')

    # Enter the folder path & remove the "" sign if it exists
    path_folder = input(r'Enter the path: ').strip("\"")

    # Add \ if necessary
    if path_folder.find("\\", -1) == -1 :
        path_folder += "\\"

    # Add image file names to list_path and sort them
    list_path = os.listdir(path_folder)
    list_path.sort(key = natural_keys)

    # Opens, identifies the given image files & add them to list_img
    list_img = []
    for i in range(0, len(list_path)) :
        list_img.append(Image.open(path_folder + list_path[i]))

    # Name file PDF
    name_file_pdf = input(r'Enter your PDF file: ')

    # Add extension .pdf if necessary
    if name_file_pdf.find(".pdf") == -1 :
        name_file_pdf += ".pdf"

    path_pdf = os.path.join(os.environ['userprofile'], "Desktop", name_file_pdf)


    # Save file PDF
    first_page = Image.open(path_folder + list_path[0])
    list_img.pop(0)
    first_page.save(path_pdf, "PDF", resolution = 100, save_all = True, append_images = list_img)

    os.system("cls")

