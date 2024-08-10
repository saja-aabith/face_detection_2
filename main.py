import cv2

cap = cv2.VideoCapture(1)
cap.set(3,640)
cap.set(4,480)

imgBackground = cv2.imread('Resources/background.png')

while True:
    success, img = cap.read()
    
    # to overlay the camera and the background image at precice location in image
    imgBackground[162:162+480, 55:55+640] = img
    
    # cv2.imshow("Camera G1", img)
    cv2.imshow("Student attendance", imgBackground)
    cv2.waitKey(1)
    
# The above code will open the camera and display the video feed in a window