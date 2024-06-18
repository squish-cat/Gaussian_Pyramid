import matplotlib.image as Image
from image_trans import imagetrans
from Gaussian_Pyramid import gaussian_pyramid
from Laplacian_Pyramid import laplacian_pyramid
from restore import imagerestore
img=Image.imread("flowergray.jpg")
img=imagetrans(img=img)
count=4
kernel_size=7
gaussian_pyramid_image_list=gaussian_pyramid(image=img,count=count,kernel_size=kernel_size,reduction_factor=0.5)
print("高斯金字塔创建完成")
laplacian_pyramid_image_list,up_sampling_image_list=laplacian_pyramid(gaussian_pyramid_image_list=gaussian_pyramid_image_list,kernel_size=kernel_size,count=count)
print("拉普拉斯金字塔创建完成")
restored_image_list=imagerestore(laplacian_pyramid_image_list=laplacian_pyramid_image_list,up_sampling_image_list=up_sampling_image_list,count=count)
print("图像重建完成")