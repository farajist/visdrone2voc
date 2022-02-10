import cv2

from os import path

def compute_new_shape(image, new_shape = (None, None), inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if new_shape[0] is None and new_shape[1] is None:
        return image

    # check to see if the width is None
    if new_shape[0] is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = new_shape[1] / float(h)
        dim = (int(w * r), new_shape[1])

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = new_shape[0] / float(w)
        dim = (new_shape[0], int(h * r))

    # return new dim
    return dim

def process_image(src_img, new_shape, dest):
    """
    """
    old_img = cv2.imread(src_img)
    new_dim = compute_new_shape(old_img, new_shape)
    new_img = cv2.resize(old_img, new_dim)
    filename = path.splitext(path.basename(src_img))[0] + '.jpg'
    target_img = path.join(dest, filename)
    cv2.imwrite(target_img, new_img)
    return {
        "file": filename,
        "path": dest,
        "new_shape": (*new_dim, 3),
        "old_shape": old_img.shape
    }
