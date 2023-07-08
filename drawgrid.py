import sys
from PIL import Image, ImageDraw
def drawgrid(grid,side):
    scale=5
    img = Image.new("RGB",((scale*side),(scale*side)),(255,255,255))
    draw = ImageDraw.Draw(img)
    for x in range(side):
        for y in range(side):
            if grid[x][y]==1:
                x0=x*scale
                y0=y*scale
                x1=x0+scale-1
                y1=y0+scale-1
                draw.rectangle(((x0,y0),(x1,y1)),(0,0,0))
    img.show()
    return
from random import choice
