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
