import numpy
import matplotlib.pyplot as plt
from gass import gass_core
from gass import convolve
from image_resize import imgresize

def laplacian_pyramid(gaussian_pyramid_image_list,kernel_size,count):
    kernel=gass_core(kernel_size)
    laplacian_pyramid_image_list=[]
    up_sampling_image_list=[]
    for i in range(0,count):
        col=numpy.size(gaussian_pyramid_image_list[count-i-1],1)
        row=numpy.size(gaussian_pyramid_image_list[count-i-1],0)
        image_resized=imgresize(image=gaussian_pyramid_image_list[count-i],row=row,col=col)
        image_conv=convolve(kernel=kernel,image=image_resized)
        difference=gaussian_pyramid_image_list[count-i-1]-image_conv;
        up_sampling_image_list.append(image_conv)
        laplacian_pyramid_image_list.append(difference)
        plt.imsave('laplacian_pyramid_image_{}.jpg'.format(count-i-1),laplacian_pyramid_image_list[i], cmap='gray')
    return laplacian_pyramid_image_list,up_sampling_image_list