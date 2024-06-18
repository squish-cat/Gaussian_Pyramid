import numpy

def search(point,nowa_length,new_length):
    i=float(0)
    point=float(point)
    nowa_length=float(nowa_length)
    new_length=float(new_length)
    while(1):
        if((i/(nowa_length-1))<=(point/(new_length-1))and((i+1)/(nowa_length-1))>=(point/(new_length-1))):
            break
        i=i+1
    i=int(i)
    return i

def imgresize(image,row,col):
    row_now=numpy.size(image,0)
    col_now=numpy.size(image,1)
    image_new=numpy.zeros((row,col),dtype=int)
    #先处理四个角
    image_new[0,0]=image[0,0]
    image_new[0,col-1]=image[0,col_now-1]
    image_new[row-1,0]=image[row_now-1,0]
    image_new[row-1,col-1]=image[row_now-1,col_now-1]
    #再处理四条边
    for i in range(1,row-1):
        pos_row=search(i,row_now,row)
        ireflect=float(i)*float(row_now-1)/float(row-1)
        value=(ireflect-float(pos_row))*image[pos_row,0] + (float(pos_row+1)-ireflect)*image[pos_row+1,0]
        image_new[i, 0]=int(value+0.5)
        value=(ireflect-float(pos_row))*image[pos_row,col_now-1] + (float(pos_row+1)-ireflect)*image[pos_row+1,col_now-1]
        image_new[i, col - 1]=int(value+0.5)
    for i in range(1, col-1):
        pos_col = search(i, col_now, col)
        ireflect = float(i) * float(col_now-1) / float(col-1)
        value = (ireflect - float(pos_col)) * image[0,pos_col] + (float(pos_col + 1) - ireflect) * image[0,pos_col + 1]
        image_new[0, i]=int(value+0.5)
        value= (ireflect - float(pos_col)) * image[row_now-1, pos_col] + (float(pos_col + 1) - ireflect) * image[row_now-1, pos_col + 1]
        image_new[row - 1, i]=int(value+0.5)
        #再处理中心区域
    for m in range(1,row-1):
        for n in range(1, col-1):
            pos_row=search(m,row_now,row)
            pos_col=search(n,col_now,col)
            a=float(n)*float(col_now-1)/float(col-1)-pos_col
            b=float(m)*float(row_now-1)/float(row-1)-pos_row
            value=(1-a)*(1-b)*image[pos_row,pos_col]+a*(1-b)*image[pos_row,pos_col+1]+b*(1-a)*image[pos_row+1,pos_col]+a*b*image[pos_row+1,pos_col+1]
            image_new[m, n]=int(value+0.5)
    return image_new



