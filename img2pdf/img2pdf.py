#!/usr/bin/env python3

from PIL import Image
import sys

def convert_img(img_path: str):
    img = Image.open(img_path, 'r')
    img_rgb = img.convert('RGB')
    img.save
    return img_rgb


def merge_img_to_pdf(imgs: list, pdf_name: str) -> None:
    image0, left_images = imgs[0], imgs[1:]
    image0.save(pdf_name, "PDF", save_all=True, resolution=100.0,\
                 append_images=left_images)


# check the # o' arguments
if len(sys.argv) < 2:
    print(f'USAGE: {sys.argv[0]} <pdf_name> <image list file>')
    exit(1)

# get pdf name
pdf_name = sys.argv[1]
if len(pdf_name) < len('a.pdf') or pdf_name[-4:] != '.pdf':
    pdf_name += '.pdf'

# extract file names
file_list_name: str = sys.argv[2]
f = open(file_list_name, 'r')
files: list = []
i: int = 0

while True:
    line: str = f.readline()

    if not line:
        break
    
    line: str = line.strip()

    print(f'img{i}: {line}')
    i += 1

    files.append(line)

f.close()

# open images and convert to RGB form
imgs: list = []
for file in files:
    imgs.append(convert_img(file))

# merge images and save as a pdf
merge_img_to_pdf(imgs, pdf_name)

# print output
print(f'Result: {pdf_name}')

