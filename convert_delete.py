import os
import cv2 

for parent, dirnames, filenames in os.walk('/home/niloofar/VGG-Face'):
    for fn in filenames:
        if fn.lower().endswith('.png'):
            img = cv2.imread(os.path.join(parent, fn))
    	    cv2.imwrite(os.path.join(parent, fn[:-3])+ 'jpg', img)
            os.remove(os.path.join(parent, fn))
