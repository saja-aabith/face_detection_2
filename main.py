import os
import cv2
import pickle

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


# load the encoding file
print('Loading encoded file...')
file = open("EncodeFile.p", 'rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIds
# print(studentIds)
print('Encoded file loaded')


# print(len(imgModeList))
while True:
    success, img = cap.read()
    
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    
    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)
    
    
    # to overlay the camera and the background image at precise location in image
    imgBackground[162:162+480, 55:55+640] = img
    if imgModeList:
        imgBackground[44:44+633, 808:808+414] = imgModeList[0]

    for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        # print(faceDis)
        matchIndex = None
        if len(faceDis) > 0:
            matchIndex = faceDis.index(min(faceDis))
        # print(matchIndex)
        if True in matches:
            name = studentIds[matchIndex]
            print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(imgBackground, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(imgBackground, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(imgBackground, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255)),
        

    # cv2.imshow("Camera G1", img)
    cv2.imshow("Student attendance", imgBackground)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
