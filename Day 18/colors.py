from colorgram import extract

# Extracts the colors from the image and puts them into a list called 'colors'
colors = extract('image.jpg', 100)

color_list = []

# The colors list contains information in addition to just the rbg values. To get the rgb values on their own in a
# separate list, we create a new list that contains only tuples of the rgb values
for x in range(len(colors)):
    rgb = colors[x].rgb
    color_list.append((rgb.r, rgb.g, rgb.b))

# The final color list has been modified to remove the several shades of white that were present
color_list = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56), (106, 140, 124), (153, 202, 227), (48, 69, 71), (131, 128, 121)]
