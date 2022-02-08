from gaugan2 import Renderer

renderer = Renderer(waiting_time=10)
renderer.run("./input_folder", "./output_folder")
renderer.create_video("./output.mp4")
