from PIL import Image

# 图片路径
image_path = 'images/size.png'

# 打开图片
image = Image.open(image_path)

# 计算新的高度，保持宽高比
new_width = 600
new_height = int((new_width / image.width) * image.height)

# 缩放图片
resized_image = image.resize((new_width, new_height))

# 保存缩放后的图片，覆盖原文件
resized_image.save(image_path)