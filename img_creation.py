from PIL import Image, ImageDraw
import numpy as np
import math
from functools import reduce

# https://pillow.readthedocs.io/en/stable/reference/Image.html

# img = Image.new('RGB', (400, 400), color = (153, 153, 155)) # monochrome

# img = Image.new('RGB', (400,400), )

# img.save('image.png') # File format based on ext, if not otherwise specified
# img.show()

def _peek_check_ints(a, b):
    pass

def create_gradient(size_a, size_b, color_a, color_b):
    # Check if Parameters correspond to specs
    if not isinstance(size_a, int):
        raise TypeError(f'Parameter size_a must be of type int, {type(size_a)} given.')
    if not isinstance(size_b, int):
        raise TypeError(f'Parameter size_b must be of type int, {type(size_b)} given.')
    if not isinstance(color_a, (int, tuple)) or not isinstance(color_b, (int, tuple)) or not type(color_a) == type(color_b):
        raise TypeError(f'color_a and color_b must be of same type, either int or tuple')
    # if isinstance(color_a, tuple) and not reduce(lambda x, y: x and y, (isinstance(z, int) for z in color_a)) or not reduce(lambda x, y: x and y, (isinstance(z, int) for z in color_b)) or not len(color_a) == 3 or not len(color_a) == len(color_b): # not checking for int values yet!
        raise TypeError(f'color a and b must contain three integers between 0 and 255')

    # initialize var for array
    pixels = []

    # calculate difference between color a and b and to estimate pixel step

    if isinstance(color_a, tuple):
        dist_a = abs(color_a[0] - color_b[0])


    else:
        dist = abs(color_a - color_b)

    # iterate over outer
    # iterate over inner
    # check previous pixels: if they exist...
    # - or, even better, discern pixel value by position... but then we need an index, don't we?

    # somehow convert to acceptable np array... (img.fromarray? Convert first?)

