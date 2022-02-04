# gaugan2-renderer

## Create videos with gaugan2

The gaugan2-renderer is a Python script that automatically uploads an image sequence to http://gaugan.org/gaugan2/ as a segmentation map, generates the output and creates a video from it.

https://user-images.githubusercontent.com/53308156/151351425-7dfdedfd-5fd4-4880-ab85-82983100e213.mp4

A example video created by Gaugan2 Renderer. On the left the input video on the right the output video.

### Usage

1. clone this repository and import the Gaugan2Renderer from gaugan2_renderer
2. install the dependencies via `pip install -r requirements.txt`

```python
from glob import glob
from gaugan2_renderer import Gaugan2Renderer

input_folder = glob("/input_folder")
output_folder = glob("./output_folder")

renderer = Gaugan2Renderer()
renderer.run(input_folder, output_folder)
renderer.create_video("./output.mp4")
```

# Api

`gaugan2_renderer.run(input_folder, output_folder)`

-   **input_folder** the folder with the segmentation maps that should be rendered
-   **output_folder** the folder with the rendered images

`gaugan2_renderer.create_video(output_path)`

-   **output_path** the path to the rendered video

# For best results, use:

-   input images with the size of 1024 px x 1024 px
-   the exact segmentation map colors
-   no anti aliasing (every pixel should have a color value specified in the **Semgmentation Map Colors**)

# Segmentation Map Colors

-   bridge: #5e5bc5
-   bush: #606e32
-   clouds: #696969
-   dirt: #6e6e28
-   fence: #706419
-   flower: #760000
-   fog: #77ba1d
-   grass: #7bc800
-   gravel: #7c32c8
-   ground-other: #7d3054
-   hill: #7ec864
-   house: #7f4502
-   mountain: #869664
-   mud: #87716f
-   pavement: #8b3027
-   platform: #8f2a91
-   river: #9364c8
-   road: #946e28
-   rock: #956432
-   roof: #9600b1
-   sand: #999900
-   sea: #9ac6da
-   sky: #9ceedd
-   snow: #9e9eaa
-   stone: #a1a164
-   straw: #a2a3eb
-   tree: #a8c832
-   wall-brick: #aad16a
-   wall-stone: #ae2974
-   wall-wood: #b0c1c3
-   water: #b1c8ff
-   wood: #b57b00
