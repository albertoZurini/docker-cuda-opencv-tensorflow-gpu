import cv2
import numpy as np

img = np.zeros((500,500,3),dtype = 'uint8')
cv2.putText(img, 'mandi', (100, 100),
		cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)

cv2.imshow('sad', img)
cv2.waitKey(0)
cv2.destroyAllWindows()