import numpy

def imagetrans(img):
    if (img.ndim==3):
        img_new = img[:, :, 0]
        img_new = numpy.squeeze(img_new)
    else:
        img_new=img
    return img_new