import cv2
import face_recognition
import pickle
import os



# importing student images
folderModePath = 'Images'
pathList = os.listdir(folderModePath)
imgList = []
studentIds = []
for path in pathList:
    img = cv2.imread(os.path.join(folderModePath, path))
    studentIds.append(os.path.splitext(path)[0])
    
    
    if img is not None:
        imgList.append(img)
    else:
        print(f"Warning: Could not read image {path}")
        
def findEncodings(imageList):
    
    encodeList = []
    for img in imageList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList



print('Encoding Started...')
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print('Encoding Complete')

file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()

