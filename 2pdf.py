from PIL import Image
import glob, os

#os.chdir("/")
im1=Image.open("42.jpeg")
im_list = []

for file in glob.glob("*.jpg"):
    print(file)
    image = Image.open(file)
    im_list.append(image)

pdf1_filename = "bbd1.pdf"

im1.save(pdf1_filename, "PDF" ,resolution=100.0, save_all=True, append_images=im_list)