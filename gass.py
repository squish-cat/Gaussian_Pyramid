import numpy
import math
sigma=1.2
def gass_core(kernel_size):
    #需要是奇数，不是奇数转化为偶数+1
    if((kernel_size & 1) == 0):
        kernel_size=kernel_size+1
    arr=numpy.zeros((kernel_size,kernel_size),dtype=float)
    center=(kernel_size-1)/2
    for m in range(0,kernel_size):
        for n in range(0,kernel_size):
            value=-(math.pow(m-center,2)+math.pow(n-center,2))
            value=value/2*math.pow(sigma,2)
            value=numpy.exp(value)
            value=value/(2*math.pi*math.pow(sigma,2))
            arr[m,n]= value

    return arr/numpy.sum(arr)


def convolve(kernel,image):
    kernel_size=numpy.size(kernel,0)
    row_len=numpy.size(image,0)
    col_len=numpy.size(image,1)
    image=numpy.pad(image,kernel_size-1)
    cup=numpy.zeros((row_len+kernel_size-1,col_len+kernel_size-1),dtype=float)
    for m in range(0,row_len+kernel_size-1):
        for n in range(0,col_len+kernel_size-1):
            image_cut=image[m:m+kernel_size,n:n+kernel_size]
            cup[m,n]=int(numpy.sum(numpy.multiply(kernel,image_cut))+0.5)
    cup_new=cup[int((kernel_size-1)/2):int(row_len+(kernel_size-1)/2),int((kernel_size-1)/2):int(col_len+(kernel_size-1)/2)]
    return cup_new

"""
img=Image.imread("test7.jpg")
img=imagetrans(img)
core=gass_core(kernel_size=7)
img_new=convolve(kernel=core,image=img);
max=img_new.max()
print(max)
img_array = (img_new * 255.0/float(max)).astype(numpy.uint8)
plt.imsave('conv2.jpg', img_array, cmap='gray')

print(core)
"""






