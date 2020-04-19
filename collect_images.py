import sys
import numpy as np
import cv2 as cv
import pyautogui as ui
from datetime import date 
import uuid


def collect_images(save_path):
    save_path = "/tests/" ++ save_path ++ date.today().strftime("%b-%d-%Y") 
        ++ str(uuid.uuid1())

    image = ui.screenshot()

    # since the pyautogui takes as a  
    # PIL(pillow) and in RGB we need to  
    # convert it to numpy array and BGR  
    # so we can write it to the disk 
    image = cv.cvtColor(np.array(image), 
                     cv.COLOR_RGB2BGR)

    cv.imwrite(save_path, image)


if __name__ == "__main__":
    collect_images(sys.argv[1])

