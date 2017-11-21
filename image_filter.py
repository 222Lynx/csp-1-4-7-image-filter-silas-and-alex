import PIL

import matplotlib.pyplot as plt # single use of plt is commented out

import os.path  

import PIL.ImageDraw 

import random          



def get_images(directory=None):

    """ Returns PIL.Image objects for all the images in directory.

    

    If directory is not specified, uses current directory.

    Returns a 2-tuple containing 

    a list with a  PIL.Image object for each image file in root_directory, and

    a list with a string filename for each image file in root_directory

    """

    

    if directory == None:

        directory = os.getcwd() # Use working directory if unspecified

        

    image_list = [] # Initialize aggregaotrs

    file_list = []

    

    directory_list = os.listdir(directory) # Get list of files

    for entry in directory_list:

        absolute_filename = os.path.join(directory, entry)
        
        # print(absolute_filename)

        try:

            image = PIL.Image.open(absolute_filename)

            file_list += [entry]

            image_list += [image]

        except IOError:

            pass # do nothing with errors tying to open non-images

    return image_list, file_list

  

def filter_one_image(original_image, skew):

    #Gets size of image

    try:

        original_image = original_image.convert('RGBA')

    except:

        pass

    height, width = original_image.size

    for x in range(height):

        for n in range(width):

            a, b, c, d = original_image.getpixel((x,n))

            a += skew

            b += skew

            c += skew

            original_image.putpixel((x,n), (a,b,c,d))

    result = PIL.Image.new('RGBA', (width,height))

    result.paste(original_image, (0,0))



    snuffles = PIL.Image.open("snuffles.PNG")

    small_snuffles = snuffles.resize((10,10))

    for x in range(height):

        for n in range(width):

                if sum(original_image.getpixel((x,n))) < 300: 

                    result.paste(small_snuffles, (x,n))

                    

    sparkle = PIL.Image.open('sparkles.png')

    small_sparkle = sparkle.resize((20,20))

    for x in range(height):

        for n in range(width):

            if random.random() < .0002: 

                result.paste(small_sparkle, (x, n))

                

    ##ghost = PIL.Image.open("Snapchat_ghost.png")

    ##ghost_resized = ghost.resize((height,width))

    ##for x in range(height):

    ##    for n in range(width):

    ##        a, b, c, d = ghost_resized.getpixel((x,n))

    ##        d = 50

    ##        ghost_resized_recolored = ghost_resized.putpixel((x,n), (a,b,c,d))

    ##result.paste(ghost_resized_recolored, (0,0))

    
    height, width = original_image.size
    god = PIL.Image.open("snufflesisagod.png")
    a= int(0.09375*width)
    b= int(0.09375*height)
    small_god = god.resize((a, b))
    d= int(height*7/8)
    c= int(width*7/8)
    result.paste(small_god, ((c,d)))

    return result

    

def filter_all_images(skew, directory=None):

    if directory == None:

        directory = os.getcwd() # Use working directory if unspecified

        

    # Create a new directory 'modified'

    new_directory = os.path.join(directory, 'modified')

    try:

        os.mkdir(new_directory)

    except OSError:

        pass # if the directory already exists, proceed  

    

    # Load all the images

    image_list, file_list = get_images(directory)  



    # Go through the images and save modified versions
    for n in range(len(image_list)):

        # Parse the filename

        print n

        filename, filetype = os.path.splitext(file_list[n])

        

        # Round the corners with default percent of radius

        curr_image = image_list[n]

        new_image = filter_one_image(curr_image, skew) 

        

        # Save the altered image, suing PNG to retain transparency

        new_image_filename = os.path.join(new_directory, filename + '.png')

        new_image.save(new_image_filename)
        
