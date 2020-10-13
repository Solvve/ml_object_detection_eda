import os
import numpy as np
from tqdm import tqdm
from PIL import Image


def get_images_metainfo(images_list: np.ndarray, images_path: str):
    """Read metadata of images

    Returns:
        List: list of dicts with keys: imagename,
            width, height, aspect_ratio.
    """
    metainfo = []

    for imagename in tqdm(images_list, total = images_list.shape[0]):
        current_meta = {
            'imagename': imagename,
        }

        image_path = os.path.join(images_path, imagename)
        width, height = Image.open(image_path).size

        current_meta['width'] = width
        current_meta['height'] = height
        current_meta['aspect_ratio'] = width/height
        metainfo.append(current_meta)

    return metainfo
