# from PIL import Image
# image = Image.open(r'C:\akhil_purpose\mask_detection\img\frame0.jpg')
# new_image = image.resize((1248, 864))
# new_image.save('C:/akhil_purpose/mask_detection/img/frame01.jpg')



# import cv2
#
# import os
#
# cap = cv2.VideoCapture('5_6208366486109555585.MOV')
#
# time_skips = float(2000) #skip every 2 seconds. You
#
# count = 0
# success,image = cap.read()
# while success:
#     print(count)
#     # image = image.resize((500, 500))
#     cv2.imwrite("C:/akhil_purpose/mask_detection/img/frame%d.jpg" % count, image)
#     cap.set(cv2.CAP_PROP_POS_MSEC,
#     (count*time_skips))
#     # move the time
#     success,image = cap.read()
#     count += 1
#
# # release after reading
# cap.release()


# Import Module

# import OS
import os
from PIL import Image
path='C:/akhil_purpose/mask_detection/img/'
path2='C:/akhil_purpose/mask_detection/imgss/'
for x in os.listdir("img"):
    print(x)

    if x.endswith(".jpg"):
        image = Image.open(path+x)
        new_image = image.resize((1248, 864))
        new_image.save(path2+x)