"""
Camera application

"""

"""
Packages
"""

#pip install opencv-python
import tkinter as tk
import cv2
from PIL import Image, ImageTk
import time 

#dlib face recognition : $pip install dlib face_recognition
import face_recognition



"""
global vars
"""




class camera:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source

        # open video source (by default this will try to open the computer webcam)
        self.vid = cv2.VideoCapture(self.video_source)

        # Create a canvas that can fit the above video source size
        self.canvas = tk.Canvas(window, width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH), height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.pack()
        

        # Button that lets the user take a snapshot
        self.btn_snapshot=tk.Button(window, text="Snapshot", width=50, command=self.snapshot)
        self.btn_snapshot.pack(anchor=tk.CENTER, expand=True)

        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 15
        self.update()


        #runs application
        self.window.mainloop()

    def snapshot(self):
        # Get a frame from the video source
        ret, frame = self.vid.read()

        if ret:
            cv2.imwrite("frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

    def update(self):
        # Get a frame from the video source
        ret, frame = self.vid.read()


        if ret:
            # Convert frame (BGR) to image (RGB)
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            ## Use face_recognition for face detection in image
            face_locations = face_recognition.face_locations(image)

            ## Draw rectangle around each face
            #color in BGR, coordinates for topleft and bottomright of rectangle
            for top, right, bottom, left in face_locations:
                cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2) 

            # Convert the image back to a PhotoImage object
            self.photo = Image.fromarray(image)
            self.photo = ImageTk.PhotoImage(image=self.photo)

            # Display the image on the canvas
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        #After processing and delay, update image
        self.window.after(self.delay, self.update)



# Create a window and pass it to the Application object
camera(tk.Tk(), "Scorpion")

