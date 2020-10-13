import os
import cv2
import numpy as np

from tqdm import tqdm
from PIL import Image


def check_images_corruption(images_list: np.ndarray, images_path: str, threshold: int=2):
    """ Check images for wrong shapes reading error & black screen images """
    for ind, imagename in tqdm(enumerate(images_list), total = images_list.shape[0]):
        image_path = os.path.join(images_path, imagename)

        image_cv2 = cv2.imread(image_path)
        width, height = Image.open(image_path).size

        message = f"Image '{imagename}' with index '{ind}' shape is wrong! " \
                  f"Shape from Pillow: {(width, height)}, shape from OpenCV: {image_cv2.shape[:2]}"

        assert width == image_cv2.shape[1] and height == image_cv2.shape[0], message
        assert np.unique(image_cv2).shape[0] >= threshold, f"Image '{imagename}' is corrupted!"

    print('Images are clear.')


def check_images_corruption_v2(images_list: np.ndarray, images_path: str, threshold: int=2):
    """Check images for wrong shapes reading
    error & black screen images.

    Returns:
        List: list of dicts with keys: imagename, shape_error, corrupted.
    """
    metainfo = []

    for imagename in tqdm(images_list, total = images_list.shape[0]):
        current_meta = {
            'imagename': imagename,
            'shape_error': None,
            'corrupted': None
        }

        image_path = os.path.join(images_path, imagename)

        image_cv2 = cv2.imread(image_path)
        width, height = Image.open(image_path).size

        if width != image_cv2.shape[1] or height != image_cv2.shape[0]:
            current_meta['shape_error'] = True

        if np.unique(image_cv2).shape[0] <= threshold:
            current_meta['corrupted'] = True

        current_meta['width'] = width
        current_meta['height'] = height
        current_meta['aspect_ratio'] = width/height
        metainfo.append(current_meta)

    return metainfo
