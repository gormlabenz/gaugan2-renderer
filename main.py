from gaugan2 import Renderer, Contours

contours = Contours(input_folder="input_origin", output_folder="input_sketch")
contours.run()

""" renderer = Renderer(waiting_time=10)
renderer.run("./input_folder", "./output_folder")
renderer.create_video("./output.mp4") """
