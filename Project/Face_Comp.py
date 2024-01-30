import face_recognition

def compare_face():
    known_image_1 = face_recognition.load_image_file("/home/pi/Software_Engineering_Project/Sid.png")
    known_image_2 = face_recognition.load_image_file("/home/pi/Software_Engineering_Project/rock.png")
    known_image_3 = face_recognition.load_image_file("/home/pi/Software_Engineering_Project/JackieChan.png")
    known_image_4 = face_recognition.load_image_file("/home/pi/Software_Engineering_Project/Obama.png")
    unknown_image = face_recognition.load_image_file("/home/pi/Software_Engineering_Project/Obama2.png")

    known_image_encoding_1 = face_recognition.face_encodings(known_image_1)[0]
    known_image_encoding_2 = face_recognition.face_encodings(known_image_2)[0]
    known_image_encoding_3 = face_recognition.face_encodings(known_image_3)[0]
    known_image_encoding_4 = face_recognition.face_encodings(known_image_4)[0]
    unknown_image_encoding = face_recognition.face_encodings(unknown_image)[0]

    if face_recognition.compare_faces([known_image_encoding_1], unknown_image_encoding)==[1]:
        result="Siddharth"

    elif face_recognition.compare_faces([known_image_encoding_2], unknown_image_encoding)==[1]:
        result="Dwayne_The_Rock_Johnson"
        
    elif face_recognition.compare_faces([known_image_encoding_3], unknown_image_encoding)==[1]:
        result="Jackie_Chan"

    elif face_recognition.compare_faces([known_image_encoding_4], unknown_image_encoding)==[1]:
        result="Ex_US_President_Barak_Obama"
    
    else:
        result="No_Match_Found"

    print(result)

