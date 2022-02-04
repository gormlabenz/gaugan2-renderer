from glob import glob
from gaugan2_renderer import Gaugan2Renderer

input_folder = glob("/input_folder")
output_folder = glob("./output_folder")

renderer = Gaugan2Renderer()
renderer.run(input_folder, output_folder)
renderer.create_video("./output.mp4")
