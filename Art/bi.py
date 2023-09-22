## By AmirHAZ(AmirHosseinAzhinehfar), i made this so you can turn your images into binary art. sick right?
import cv2

image_path = 'hello.jpg'
image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

original_width, original_height = image_gray.shape[1], image_gray.shape[0]
aspect_ratio = original_width / original_height
new_height = 150
new_width = int(new_height * aspect_ratio)
image_resized_aspect = cv2.resize(image_gray, (new_width, new_height))

blurred_aspect = cv2.GaussianBlur(image_resized_aspect, (5, 5), 0)
adaptive_thresh_aspect = cv2.adaptiveThreshold(blurred_aspect, 1, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2)

binary_representation_aspect = '\n'.join(''.join('1' if pixel else '0' for pixel in row) for row in adaptive_thresh_aspect)

with open('Art.txt', 'w') as file:
    file.write(binary_representation_aspect)
