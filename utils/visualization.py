import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


def display_multiple_img(images: np.ndarray, images_path: str, cols: int = 2):
    """ Function for multiple images visualiztaion """
    assert (images.shape[0] % cols) == 0

    for imagename_pair in images.reshape(-1, cols):
        _, axs = plt.subplots(nrows = 1, ncols = cols, figsize = (10, 10))

        for ind, imagename in enumerate(imagename_pair):
            image = cv2.imread(
                os.path.join(images_path, imagename)
            )
            axs[ind].imshow(image[:,:,::-1])
            axs[ind].set_title(imagename + ' ' + str(image.shape))
            axs[ind].axis('off')
