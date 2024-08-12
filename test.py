import face_recognition

# Load a sample picture and learn how to recognize it.
image = face_recognition.load_image_file("Images/Saja.jpg")
face_locations = face_recognition.face_locations(image)

print("Found {} face(s) in this photograph.".format(len(face_locations)))