import cv2
import numpy as np

image = cv2.imread('Inja Adress Image Gharar migire', cv2.IMREAD_GRAYSCALE) #besoorat grayscale read mishe

tasvir_matt = cv2.GaussianBlur(image, (5, 5), 0) #guassianblur mindazim ro image

edges = cv2.Canny(tasvir_matt,30, 100) #az canny edge detection vase detect kardan labe ha estefade mikonim


cv2.imshow('Original Image', image) #aks asli ro namayesh midim

cv2.imshow('Edge Detected Image', edges) #aks edge detect shode ro namayesh midim

cv2.waitKey(0)
cv2.destroyAllWindows()

#AlirezaTimas
