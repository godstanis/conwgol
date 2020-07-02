from PIL import Image
import sys

def countN(x: int, y: int, fld: list) -> int:
    """ Count all alive neighbours """

    mw, mh = len(fld), len(fld[0])
    """ check 3 row elements above, check 2 sides, check 3 row elements below """
    return fld[(x-1) % mw][(y-1)% mh] + fld[x][(y-1)% mh] + fld[(x+1) % mw][(y-1)% mh] +\
        fld[(x-1) % mw][y] + fld[(x+1) % mw][y] +\
        fld[(x-1) % mw][(y+1)% mh] + fld[x][(y+1)% mh] + fld[(x+1) % mw][(y+1)% mh]

def generateNext(fld: list):
    """ Write new generation to field based on field's initial state """

    deathrow, liferow, neighbours = [], [], 0
    for i, row in enumerate(fld):
        for j, el in enumerate(row):
            neighbours = countN(i, j, fld)
            if el == 1:
                """ Any live cell with two or three live neighbours survives. """
                if neighbours != 2 and neighbours != 3:
                    deathrow.append([i,j])
                continue
            if neighbours == 3:
                """ Any dead cell with three live neighbours becomes a live cell. """
                liferow.append([i,j])
    
    for v in deathrow:
        fld[v[0]][v[1]] = 0
    for v in liferow:
        fld[v[0]][v[1]] = 1

def fieldToImg(lst: int) -> Image:
    """ Transform field 2-dimentional list to black/white pixel image """

    img = Image.new('RGB', (len(lst), len(lst[0])), color = 'white')
    pixels = img.load()
    for i, row in enumerate(lst):
        for j, el in enumerate(row):
            if el == 1:
                pixels[i, j] = (0, 0, 0)
            else:
                pixels[i, j] = (255, 255, 255)
    return img

def imagesToGif(fname: str, imgs: list):
    imgs[0].save(fname, save_all=True, append_images=imgs[1:], optimize=False, duration=0, loop=0)

def imageToField(img: Image) -> list:
    """ Transform Image to 2-dimentional list where black pixel is 1 and white is 0 """

    lst = []
    pixels = img.load()
    width, height = img.size
    for x in range(width):
        lel = []
        for y in range(height):
            if pixels[x, y] == (0, 0, 0):
                lel.append(1)
            else:
                lel.append(0)
        lst.append(lel)

    return lst

def imgToGenImgs(field: list, gns: int) -> list:
    """ Create list of generations in Image format based on field's initial state """

    images = []
    for _ in range(gns):
        images.append(fieldToImg(field))
        generateNext(field)
    return images

def imgToGif(src: Image, dst: str, gns: int):
    """ Create and save animated gif, based on an initial state, retrieved from source image """
    
    lst = imageToField(src)
    imagesToGif(dst, imgToGenImgs(lst, gns))
