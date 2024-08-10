import os
import cv2

cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)

imgBackground = cv2.imread('Resources/background.png')

# importing the mode images into a list
folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []
for path in modePathList:
    img = cv2.imread(os.path.join(folderModePath, path))
    if img is not None:
        imgModeList.append(img)
    else:
        print(f"Warning: Could not read image {path}")

# print(len(imgModeList))

while True:
    success, img = cap.read()
    
    # to overlay the camera and the background image at precise location in image
    imgBackground[162:162+480, 55:55+640] = img
    if imgModeList:
        imgBackground[44:44+633, 808:808+414] = imgModeList[0]

    # cv2.imshow("Camera G1", img)
    cv2.imshow("Student attendance", imgBackground)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()