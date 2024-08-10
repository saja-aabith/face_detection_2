import cv2

cap = cv2.VideoCapture(1)
cap.set(3,1280)
cap.set(4,720)

imgBackground = cv2.imread('Resources/background.png')

while True:
    success, img = cap.read()
    cv2.imshow("Camera attendance", img)
    cv2.imshow("Face")
    cv2.waitKey(1)
    
# The above code will open the camera and display the video feed in a window