import os
import cv2


dataDir = "/media/zj/data3-ext4/data-sets/gx-armors-datasets/yolo_datav5/images/"
saveDir = "/media/zj/data3-ext4/data-sets/gx-armors-datasets/yolo_datav5/images-new/"

if not os.path.exists(saveDir):
    os.makedirs(saveDir)

for one_pic in os.listdir(dataDir):
    one_path = os.path.join(dataDir, one_pic)
    one_img = cv2.imread(one_path)
    new_path = os.path.join(saveDir, one_pic)
    cv2.imwrite(new_path, one_img)
