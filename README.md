# gaugan2-renderer
## Create videos with gaugan2
The gaugan2-renderer is a Python script that automatically uploads an image sequence to http://gaugan.org/gaugan2/ as a segmentation map, generates the output and creates a video from it.
![Interface of the Gaugan2 Editor](https://miro.medium.com/max/2000/1*TlEbWHn6_CrUysjOR1IBiQ.png)
### Usage
Clone this repository and import the Gaugan2Renderer from gaugan2_renderer
```python
from glob import glob
from gaugan2_renderer import Gaugan2Renderer

input_images = glob("/input_images_1/*")
output_images = glob("./output_images_1")

Renderer = Gaugan2Renderer()
Renderer.run(input_images, output_images)
Renderer.create_video("./output_1.mp4")
```
# Api
```gaugan2_renderer.run(input_folder, output_folder)```
-  **input_folder** the folder with the segmentation maps that should be rendered
-  **output_folder** the folder with the rendered images

```gaugan2_renderer.create_video(output_path)```
- **output_path** the path to the rendered video
# For best results, use:
- Images with the size of 1024 px x 1024 px
- Use the exact segmentation map colors 
- No anti aliasing (no pixel should have a different color value than specified in the semgmentation map)
# Segmentation Map Colors

-  bridge: #5e5bc5
-  bush: #606e32
-  clouds: #696969
-  dirt: #6e6e28
-  fence: #706419
-  flower: #760000
-  fog: #77ba1d
-  grass: #7bc800
-  gravel: #7c32c8
-  ground-other: #7d3054
-  hill: #7ec864
-  house: #7f4502
-  mountain: #869664
-  mud: #87716f
-  pavement: #8b3027
-  platform: #8f2a91
-  river: #9364c8
-  road: #946e28
-  rock: #956432
-  roof: #9600b1
-  sand: #999900
-  sea: #9ac6da
-  sky: #9ceedd
-  snow: #9e9eaa
-  stone: #a1a164
-  straw: #a2a3eb
-  tree: #a8c832
-  wall-brick: #aad16a
-  wall-stone: #ae2974
-  wall-wood: #b0c1c3
-  water: #b1c8ff
-  wood: #b57b00

