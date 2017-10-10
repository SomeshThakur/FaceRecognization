import cv2
import sys
from Tkinter import *
from tkFileDialog   import askopenfilename 
     
imagepath=''

def callback():
    imagepath= askopenfilename()
    recognize(imagepath) 

def recognize(imagepath):
    # Get user supplied values
    cascPath = "haarcascade_frontalface_default.xml"

    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)

    # Read the image
    image = cv2.imread(imagepath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
         gray,
         scaleFactor=1.8,
         minNeighbors=5,
    minSize=(30, 30)
    #flags = cv2.CV_HAAR_SCALE_IMAGE
    )
    
    print("Found {0} face(s)!".format(len(faces)))

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow("Face(s) found", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def quit():
    root.destroy()

root = Tk()
root.title("Face Recognization")
root.geometry('400x200')
Label(root, 
		 text="-------------Face Recognizer-----------",
		 fg = "blue",
		 bg = "yellow",
		 font = "Helvetica 16 bold italic").pack()
Label(root, 
		 text="By Somesh Thakur and Md. Hassain Shareef",
		 fg = "blue",
		 font = "Verdana 10 bold").pack()
Button(root,text='Select Image', command=callback,fg="blue").pack(fill=X,padx=10,pady=20)
Button(root,text='Quit', command=quit,fg="red").pack(fill=X,padx=10,pady=10)
root.mainloop()  


