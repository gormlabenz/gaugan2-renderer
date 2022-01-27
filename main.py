import os
from glob import glob

from gaugan2_renderer import Gaugan2Renderer

Renderer = Gaugan2Renderer()
Renderer.run(glob(os.getcwd() + "/input_images_5/*"), "./output_images_5")
Renderer.create_video("./output_5.mp4")
