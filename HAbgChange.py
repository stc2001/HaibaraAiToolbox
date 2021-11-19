import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib import animation
import paddlehub as hub
from PIL import Image, ImageSequence
import numpy as np
import os
import paddle
from tkinter.filedialog import askopenfilename
paddle.enable_static()
# 测试图片路径和输出路径
test_path = ''  #按需更改路径
output_path = ''  #按需更改路径
filePath=str(askopenfilename(filetypes=[("靓照", "*.jpg *.png *.jpeg"), ("所有文件", "*.*")]))
# 待预测图片
test_img_path = [filePath]  #按需更改文件名
test_img_path = [test_path + img for img in test_img_path]

module = hub.Module(name="deeplabv3p_xception65_humanseg")
input_dict = {"image": test_img_path}

# execute predict and print the result
results = module.segmentation(data=input_dict)
for result in results:
    print(result)

def SelfShotFunction():
# 预测结果展示
    out_img_path = 'humanseg_output'+os.sep + os.path.basename(test_img_path[0]).split('.')[0] + '.png'   #输出图片的位置
    img = mpimg.imread(out_img_path)
    plt.figure(figsize=(10,10))
    plt.imshow(img)
    plt.axis('off')
    plt.show()
