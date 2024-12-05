from random import choice
from os import listdir
from attentionme import *
import cv2

images = listdir('sample_images')
image_path = 'sample_images/' + choice(images)
image = cv2.imread(image_path)
cv2.imwrite('image_outputs/original_image.png', image)

# 객체 확대 기능
enlargement(image_path, 'image_outputs/enlarged_image.png', 1.2)

# 줌인 기능
zoom_in(image_path, 'image_outputs/zoomed_image.png')

# crop 기능
crop(image_path, 'image_outputs/cropped_image.png')

# 배경 밝기 조절 기능 (밝게)
adjust_brightness(image_path, 'image_outputs/brighten_image.png', 1.4)

# 배경 밝기 조절 기능 (어둡게)
adjust_brightness(image_path, 'image_outputs/darken_image.png', 0.6)

# 강조 기능
add_pointed_person(image_path, 'image_outputs/pointed_image.png', 4, (0, 0, 255))

# 배경 제거 기능
remove_background(image_path, 'image_outputs/removed_background_image.png')
