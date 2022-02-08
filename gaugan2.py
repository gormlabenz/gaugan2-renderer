import base64
import os
import re
import time
from glob import glob
from itertools import zip_longest

import cv2
import imageio
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from tqdm import tqdm
from webdriver_manager.firefox import GeckoDriverManager


def natural_sort(l):
    def convert(text): return int(text) if text.isdigit() else text.lower()
    def alphanum_key(key): return [convert(c)
                                   for c in re.split('([0-9]+)', key)]
    return sorted(l, key=alphanum_key)


class Renderer:
    def __init__(self, waiting_time=5):
        self.waiting_time = waiting_time
        self.output_images = []
        firefox_options = Options()
        firefox_options.headless = True

        self.driver = webdriver.Firefox(
            executable_path=GeckoDriverManager().install(), options=firefox_options)

    def open(self):
        self.driver.get("http://gaugan.org/gaugan2/")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "viewport"))
        )
        self.close_popups()

    def close_popups(self):
        if close_button := self.driver.find_element(
            By.XPATH, "/html/body/div[2]/div/header/button"
        ):
            close_button.click()

        if terms_and_conditions := self.driver.find_element(
            By.XPATH, '//*[@id="myCheck"]'
        ):
            terms_and_conditions.click()

    def download_image(self, file_path):
        output_canvas = self.driver.find_element(
            By.ID, 'output')
        canvas_base64 = self.driver.execute_script(
            "return arguments[0].toDataURL('image/png').substring(21);", output_canvas)
        canvas_png = base64.b64decode(canvas_base64)

        with open(file_path, 'wb') as f:
            f.write(canvas_png)

    def upload(self, fileid, loadid, file_path):
        self.driver.find_element(
            By.XPATH, f'//*[@id="{fileid}"]').send_keys(file_path)
        self.driver.find_element(
            By.XPATH, f'//*[@id="{loadid}"]').click()

    def render_image(self):
        self.driver.find_element(
            By.XPATH, '//*[@id="render"]').click()

    def run(self, output_path, segmentation_map_folder=None, sketch_folder=None):
        self.open()
        os.makedirs(output_path, exist_ok=True)

        if segmentation_map_folder is None:
            segmentation_map_folder = []
        if sketch_folder is None:
            sketch_folder = []

        self.segmentation_map_paths = glob(
            segmentation_map_folder + "/*.png")
        natural_sort(self.segmentation_map_paths)

        self.sketch_paths = glob(
            sketch_folder + "/*.png")
        natural_sort(self.sketch_paths)

        print(self.segmentation_map_paths)

        if len(self.sketch_paths) != 0:
            self.driver.find_element(
                By.XPATH, '//*[@id="enable_edge"]').click()

        for index, (segmentation_map, sketch) in tqdm(enumerate(zip_longest(self.segmentation_map_paths, self.sketch_paths, fillvalue=None))):
            if segmentation_map:
                segmentation_map = os.path.abspath(segmentation_map)
                self.upload('segmapfile', 'btnSegmapLoad', segmentation_map)

            if sketch:
                sketch = os.path.abspath(sketch)
                self.upload('sketchfile', 'btnSketchLoad', sketch)

            self.render_image()

            output_image = os.path.join(output_path,
                                        str(index) + '.png')

            time.sleep(self.waiting_time)
            self.download_image(output_image)
            self.output_images.append(output_image)

        self.driver.close()

    def create_video(self, output_video):
        images = [imageio.imread(image) for image in self.output_images]
        imageio.mimsave(output_video, images, fps=10)


class Editor:
    def __init__(self, input_folder, output_folder):
        self.input_folder = input_folder
        self.output_folder = output_folder

        os.makedirs(self.output_folder, exist_ok=True)

        self.segmentation_map_paths = glob(input_folder + "/*.png")

    def run(self):

        for file_path in tqdm(self.segmentation_map_paths):
            file_path = os.path.abspath(file_path)
            basename = os.path.basename(file_path)
            output_image_path = os.path.join(self.output_folder,
                                             basename)

            image = self.edit(imageio.imread(file_path))
            imageio.imwrite(output_image_path, image)

    def edit(self, image):
        return image


class Contours(Editor):
    def __init__(self, input_folder, output_folder):
        super().__init__(input_folder, output_folder)

    def edit(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.GaussianBlur(image, (81, 81), 0)
        ret, image = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(
            image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        mask = np.zeros((*image.shape, 4), dtype=np.uint8)
        image = cv2.drawContours(
            mask, contours, -1, (0, 0, 0, 255), 1)

        image = image[4:-4, 4:-4]
        # add 4 pixel border around image
        image = cv2.copyMakeBorder(
            image, 4, 4, 4, 4, cv2.BORDER_CONSTANT, value=(0, 0, 0))

        return image


if __name__ == "__main__":
    contours = Contours(input_folder="input",
                        output_folder="input_sketch")
    contours.run()
