import cv2

from os import path

def process_image(src_img, new_shape, dest):
    """
    """
    old_img = cv2.imread(src_img)
    new_img = cv2.resize(old_img, (new_shape[0], new_shape[1]))
    filename = path.splitext(path.basename(src_img))[0] + '.jpg'
    target_img = path.join(dest, filename)
    cv2.imwrite(target_img, new_img)

    return {
        "file": filename,
        "path": dest,
        "new_shape": new_img.shape,
        "old_shape": old_img.shape
    }
