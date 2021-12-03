import numpy as np
import matplotlib.pyplot as plt
from scipy import misc

np.random.seed(0)
# create a random image with int values between 0 and 255
image = np.random.randint(0, 255, size=(100, 100, 3), dtype=np.uint8)


# create a function named 'show' that takes an image as input and displays it
def show(image):
    plt.imshow(image)
    plt.show()

#TODO : find how to really choos a color and not a shade of gray
def modifyRandomlyWithAColour(image, colour, frequency=50):
  # do a loop to color random coordinates in the image with the colour
  
  for i in range(0, image.shape[0]):
      for j in range(0, image.shape[1]):
        if(np.random.randint(0,100) < frequency):
          image[i, j] = colour
    
  show(image)
    
# call the function 'modifyRandomlyWithAColour' with the image and a random colour
modifyRandomlyWithAColour(image, 125)


