# 同时添加如下代码, 这样每次环境(kernel)启动的时候只要运行下方代码即可: 

import sys 
sys.path.append('/home/aistudio/external-libraries')


import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('data/nezha.jpeg',1)
# img_np = np.array(img) 
plt.hist(img.reshape([-1]),256,[0,256]);
plt.show()


import cv2
# import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('data/nezha.jpeg',0)
histr = cv2.calcHist([img],[0],None,[256],[0,256]) #hist是一个shape为(256,1)的数组，表示0-255每个像素值对应的像素个数，下标即为相应的像素值
plt.plot(histr,color = 'b')
plt.xlim([0,256])
plt.show()

import cv2
from matplotlib import pyplot as plt
img = cv2.imread('data/nezha.jpeg',1) 
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    #hist是一个shape为(256,1)的数组，表示0-255每个像素值对应的像素个数，下标即为相应的像素值
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()

import sys
import numpy as np
import cv2
import matplotlib.pyplot as plt

def main():
    img=cv2.imread('data/nezha.jpeg',0)
    #得到计算灰度直方图的值
    n = np.array(img)
    xy=xygray(img)   

    #画出灰度直方图
    x_range=range(256)
    plt.plot(x_range,xy,"r",linewidth=2,c='black')
    #设置坐标轴的范围
    y_maxValue=np.max(xy)
    plt.axis([0,255,0,y_maxValue])
    #设置坐标轴的标签
    plt.xlabel('gray Level')
    plt.ylabel("number of pixels")
    plt.show()

def xygray(img):
    #得到高和宽
    rows,cols=img.shape
    print(img.shape)
    #存储灰度直方图
    xy=np.zeros([256],np.uint64)
    for r in range(rows):
        for c in range(cols):
            xy[img[r][c]] += 1
    #返回一维ndarry
    print(xy.sum())
    return xy

main()