import enroll,spreadsheet,emailing,recognition
ch=input("Enter E for Enroll or R for Recognition : \n")

if(ch=='E' or ch=='e'):
    name = input("Enter your name : ")
    enroll.enroll_via_camera(name)
    
elif(ch=='R' or ch=='r'):
    spreadsheet.none()
    
    for x in range(2):
        recognition.load_facial_encodings_and_names_from_memory()
        recognition.run_recognition()
else:
    print("Invalid Choice !!")


# DEVELOPERS : SNEHA M, SATHYANARAYAN S


