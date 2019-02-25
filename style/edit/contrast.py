img = cv2.imread('Dog.jpg', 1)

def increase_contrast(img, value=30):
	lab= cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
	l, a, b = cv2.split(lab)

	#-----Applying CLAHE to L-channel-------------------------------------------
	clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
	cl = clahe.apply(l)

	limg = cv2.merge((cl,a,b))

	return cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
