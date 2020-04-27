import sys
import numpy as np
import cv2 as cv
import pyautogui as ui
from datetime import date 
import uuid
import time

def collect_images(save_path, n_pictures):
    for i in range(n_pictures):
        full_path = "test_data/%s/%s.%s" % (save_path, uuid.uuid1(),"png")
        image = ui.screenshot()

        # since the pyautogui takes as a  
        # PIL(pillow) and in RGB we need to  
        # convert it to numpy array and BGR  
        # so we can write it to the disk 
        image = cv.cvtColor(np.array(image), cv.COLOR_RGB2BGR)
        cv.imwrite(full_path, image)
        time.sleep(3)


if __name__ == "__main__":
    save_path = sys.argv[1]
    n_pictures = int(sys.argv[2])
    print("\n\nPictures will be saved to: \n\t test_date/%s/<uuid>" % (save_path))
    print("\n Approximate runtime: \n\t%s minutes\n\n" % (n_pictures*3/60))
    collect_images(save_path, n_pictures)

