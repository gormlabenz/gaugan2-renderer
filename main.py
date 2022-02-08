from gaugan2_renderer import Gaugan2Renderer

renderer = Gaugan2Renderer(waiting_time=10)
renderer.run("./input_folder", "./output_folder")
renderer.create_video("./output.mp4")
