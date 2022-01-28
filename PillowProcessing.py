from PIL import Image
import os


imagetypes = ['.jpg', '.png', '.tiff', '.bmp', '.webm', '.jpeg']
requiredtype =  '.jpeg'
imgdirname = r"D:\GoogleCertificate\Main Exercises\Exercise 1\Image Processing\images"
newimagelocation = r"D:\GoogleCertificate\Main Exercises\Exercise 1\Image Processing\NewImages"
for dirpath, dirnames, filenames in os.walk(imgdirname):

    for file in filenames:

        rawfilename, extension = os.path.splitext(file)

        if extension in imagetypes:
            newfilename = os.path.join(newimagelocation, rawfilename + requiredtype)
            im = Image.open(os.path.join(dirpath, file))
            im.resize((128,128)).convert('RGB').rotate(90).save(newfilename, "JPEG")
