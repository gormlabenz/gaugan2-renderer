import os
from glob import glob

from gaugan2_renderer import Gaugan2Renderer

Renderer = Gaugan2Renderer()
Renderer.run(glob(os.getcwd() + "/input_images_1/*"), "./output_images_1")
Renderer.create_video("./output_1.mp4")
