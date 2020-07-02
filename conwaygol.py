import sys
from PIL import Image
from pkg.cnwgl import imgToGif

desc = '''
Usage:
	conwaygol <input_image> <output_gif> [generations]

Options:
	input_image  (required)     Image path of the first Conway's generation (black pixel for live cells and white ones for dead)
	output_gif   (required)     Gif image path where the resulting animation will be placed
	generations  (default: 50)  Number of generations (gif frames) to output

'''

def parseArgs() -> (str, str, int):
    if len(sys.argv[1:]) < 2:
        print(desc)
        sys.exit(126)

    src, dst, gns = sys.argv[1], sys.argv[2], 50

    if len(sys.argv[1:]) == 3:
        try:
            gns = int(sys.argv[3])
        except:
            print("Error: [generations] parameter must be integer\n", desc)
            sys.exit(126)
    return src, dst, gns

src, dst, gns = parseArgs()

print("Processing...")
imgToGif(Image.open(src), dst, gns)
print('File generated at \'{}\''.format(dst))
