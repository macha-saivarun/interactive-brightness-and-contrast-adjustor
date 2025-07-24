import cv2
import numpy as np

def apply_brightness_contrast(input_img, brightness=0, contrast=0):
    if brightness != 0:
        shadow = brightness if brightness > 0 else 0
        highlight = 255 if brightness > 0 else 255 + brightness
        alpha_b = (highlight - shadow) / 255
        gamma_b = shadow
        buf = cv2.addWeighted(input_img, alpha_b, input_img, 0, gamma_b)
    else:
        buf = input_img.copy()

    if contrast != 0:
        f = 131 * (contrast + 127) / (127 * (131 - contrast))
        alpha_c = f
        gamma_c = 127*(1 - f)
        buf = cv2.addWeighted(buf, alpha_c, buf, 0, gamma_c)

    return buf

def nothing(x):
    pass

image = cv2.imread('image.jpg')
cv2.namedWindow('Adjuster')

cv2.createTrackbar('Brightness', 'Adjuster', 127, 254, nothing)
cv2.createTrackbar('Contrast', 'Adjuster', 127, 254, nothing)

while True:
    brightness = cv2.getTrackbarPos('Brightness', 'Adjuster') - 127
    contrast = cv2.getTrackbarPos('Contrast', 'Adjuster') - 127
    adjusted = apply_brightness_contrast(image, brightness, contrast)
    cv2.imshow('Adjuster', adjusted)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
