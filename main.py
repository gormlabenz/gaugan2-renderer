import os
from glob import glob

from gaugan2_renderer import Gaugan2Renderer

Renderer = Gaugan2Renderer()
Renderer.run(glob(os.getcwd() + "/input_images_3/*"), "./output_images_3")
