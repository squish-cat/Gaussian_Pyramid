import numpy
import matplotlib.pyplot as plt
from gass import gass_core
from gass import convolve
from image_resize import imgresize

def gaussian_pyramid(image,count,kernel_size,reduction_factor):
    kernel=gass_core(kernel_size);
    gaussian_pyramid_image_list=[image]
    plt.imsave('gaussian_pyramid_image_0.jpg', gaussian_pyramid_image_list[0], cmap='gray')
    for i in range(0,count):
        row_len_origin = numpy.size(gaussian_pyramid_image_list[i], 0)
        col_len_origin = numpy.size(gaussian_pyramid_image_list[i], 1)
        image_conv=convolve(kernel=kernel,image=gaussian_pyramid_image_list[i])
        row_len_new=int(row_len_origin*reduction_factor+0.5)
        col_len_new=int(col_len_origin*reduction_factor+0.5)
        #下采样
        image_down_sampling=imgresize(image=image_conv,row=row_len_new,col=col_len_new)
        gaussian_pyramid_image_list.append(image_down_sampling)
        plt.imsave('gaussian_pyramid_image_{}.jpg'.format(i+1), gaussian_pyramid_image_list[i+1], cmap='gray')
    return gaussian_pyramid_image_list