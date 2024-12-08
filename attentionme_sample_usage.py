from attentionme import *

image_path = 'sample_images/group1.jpg'

# 객체 확대 기능
enlargement(image_path, 'image_outputs/enlarged_image.png', 1.5)

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
