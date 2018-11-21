# -*- coding:utf-8 -*-
# 导入cv模块
import cv2 as cv
"""
安装一下模块
pip install --upgrade setuptools
pip install numpy Matplotlib
pip install opencv-python
"""
# 读取图像，支持 bmp、jpg、png、tiff 等常用格式
# r 显式声明字符串不用转义
img = cv.imread("123.jpg")
# 创建窗口并显示图像
cv.namedWindow("Image")
cv.imshow("Image", img)
cv.waitKey(0)
# 释放窗口
cv2.destroyAllWindows()