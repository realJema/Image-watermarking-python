'''
Name: realjema
date: 17-03-2020
program: watermarker
description: This is a program to add a watermark image onto another image. It permits bulk image watermarking which is very fast and efficient. 
'''

from os import listdir
from PIL import Image

# add the paths to the images here 
path = r'C:\Users\realjema\Downloads'
logo = r'C:\Users\realjema\Documents\PS\OBILI\lg.png'

def watermark_photo(input_image, watermark_image):
    '''
    watermarking the images 
    INPUT: 
    input_image which is the image to watermark
    watermark__image which is the logo we are trying to add
    OUTPUT:
    the input_image is updated
    '''
    base_image = Image.open(input_image)
    watermark = Image.open(watermark_image)


    # we have to resize the logo to fit in the new image     
    base_image_height, base_image_width = base_image.size
    watermark_height, watermark_width = watermark.size
    new_height = int(base_image_height/10) # we divide by 10 to reduce the size of the logo
    new_watermark = watermark.resize((new_height, new_height)) #resize logo, since its a square image we use just the height 
    
    # this permits the watermark to be positioned at the top right corner of the image 
    # taking into consideration the dimensions of the image 
    position = (int(base_image_width - (0.2 * base_image_width)), int(base_image_height - (0.8 * base_image_height))) # X and Y axis we subtract 20% and 80% respectively

    # adding the logo to the images 
    base_image.paste(new_watermark, position, mask=new_watermark)
    # base_image.show() # this is to display the image once its done
    base_image.save(input_image) # we modify the original image 

def list_files(directory, extension):
    'Get the files with the extension specified'
    return (f for f in listdir(path) if f.endswith('.' + extension))

if __name__ == '__main__':
    # watermark_photo('lighthouse.jpg', 'output.jpg', 'logo.png', position=(0,0))
    files = list_files(path, "jpg")
    for file in files:
        # watermark each files
        print('watermarking ' + file)
        watermark_photo(path + '\\' + file, logo) # you have to pass the path to the file aswell