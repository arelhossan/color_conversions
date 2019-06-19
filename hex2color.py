import math

colors={"white":    (255, 255, 255),
        "black":    (0,   0,   0),
        "red":      (255, 0,   0),
        "blue":     (0,   0,   255),
        "green":    (0,   128, 0),
        "yellow":   (255, 255, 0),
        "purple":   (128, 0,   128),
        "brown":    (139, 69,  19),
        "orange":   (255, 165, 0),
        "gray":     (175, 175, 175)}

def hexcode2color(hexcode):
    rgb=tuple(int(hexcode[i:i + 2], 16) for i in (0, 2, 4))
    closest_color=("",442) #442 is the worst root-square-error in this case
    for color in colors:
        redD=colors[color][0]-rgb[0]
        greenD=colors[color][1]-rgb[1]
        blueD=colors[color][2]-rgb[2]
        distance=math.sqrt(redD**2 + greenD**2 + blueD**2)
        if distance < closest_color[1]:
            closest_color=(color,distance)
    return closest_color[0]


def color2hexcode(color):
    hexcode="".join([hex(i).replace("0x","") if i !=0 else "00" for i in colors[color] ])
    return hexcode


