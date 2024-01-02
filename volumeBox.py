#Write a function to calculate volume of a box with appropriate default values for its parameters. Your function should have the following input parameters:
#      a) length of box     b) width of box    c) height of box

def volume_box(length, width, height):
    volume = length*width*height
    return volume

print(volume_box(15,8,20))
