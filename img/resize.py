import cv2

for i in range(1,9):
	img = cv2.resize(cv2.imread(f"./slide{i}.jpg"), (100,100))
	cv2.imwrite(f'sslide{i}.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
