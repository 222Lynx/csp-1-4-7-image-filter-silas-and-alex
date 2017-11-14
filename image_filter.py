import PIL
import matplotlib.pyplot as plt
import os.path
import PIL.ImageDraw

# you can assume that I will run the program in the same directory as the file

def new_filter(filename):
    
    directory = os.getcwd() # Use working directory 
    absolute_filename = os.path.join(directory, filename) # get the absolute filename
    image = PIL.Image.open(absolute_filename) # create an image object from the file
    
    # your code goes here
    
    plt.imshow(image)