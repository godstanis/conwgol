# conwgol
:building_construction: Simple Conway's game of life implementation in Python3

<hr>

### Description

Conway's game of life is implemented in pkg/cnwgl.py file. There are some functions, working with list map generations and some upper level helpers to interact with images creation.

### Usage

You can run it on your input images, here is the CLI definition:

```python
Usage:
    conwaygol.py <input_image> <output_gif> [generations]

Options:
    input_image  (required)     Image path of the first Conway's generation (black pixel for
                                live cells and white ones for dead)
    output_gif   (required)     Gif image path where the resulting animation will be placed
    generations  (default: 50)  Number of generations (gif frames) to output
```

Usage example:
`python3 conwaygol.py input.png output.gif 300`

#### Example (upscaled) of converted `image.png`:

<img src="https://github.com/godstanis/conwgol/blob/master/.github/media/example_01.gif?raw=true" width="100%">
