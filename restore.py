import numpy
import matplotlib.pyplot as plt

def imagerestore(laplacian_pyramid_image_list,up_sampling_image_list,count):
    restored_image_list=[]
    for i in range(count):
        image_restored=laplacian_pyramid_image_list[i]+up_sampling_image_list[i]
        image_restored=image_restored.astype(numpy.uint8)
        restored_image_list.append(image_restored)
        plt.imsave('restored_image_{}.jpg'.format(count - i - 1), restored_image_list[i], cmap='gray')
    return  restored_image_list