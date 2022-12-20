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
import face_recognition #TODO - use dlib.cnn_face_detection_model_v1



"""
Global vars
"""
# Keep track of the button state on/off
#global is_on
is_on = True



class camera:
    """
    Class that takes video frame, and displays it in tkinter window.
    Allows user to take snapshots that are timestamped and see information about person in frame 
    """
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source

        # open video source (by default this will try to open the computer webcam)
        self.vid = cv2.VideoCapture(self.video_source)

        # Create a canvas that can fit the above video source size
        self.canvas = tk.Canvas(window, width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH), height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.grid()
        

        #adding data area
        frame_data = tk.Frame(window)
        frame_data.grid(row=0, column=1)      
        bg_color = "" 
        fg_color = "black"
        #Person Name
        person_label = tk.Label(frame_data,             #label
                            text = "Identity: ",
                            fg=fg_color)
        person_label.grid(row=0, column=0, sticky=tk.E)

        person_name = tk.Label(frame_data,              #name
                            text = "Tux Torvaldas",
                            fg=fg_color)
        person_name.grid(row=0, column=1, sticky=tk.W)

        #Person DOB
        dob_label = tk.Label(frame_data,                #label
                            text = "Date of Birth: ",
                            fg=fg_color)
        dob_label.grid(row=1, column=0, sticky=tk.E)

        person_dob= tk.Label(frame_data,                #dob
                            text = "08/25/1991",
                            fg=fg_color)
        person_dob.grid(row=1, column=1, sticky=tk.W)

        #Person Gender 
        label_gender = tk.Label(frame_data,             #label
                            text = "Gender: ",
                            fg=fg_color)
        label_gender.grid(row=2, column=0, sticky=tk.E)

        person_gender = tk.Label(frame_data,            #gender
                            text = "M",
                            fg=fg_color)
        person_gender.grid(row=2, column=1, sticky=tk.W)


        #Person Address
        address_label = tk.Label(frame_data,             #label
                            text = "Address: ",
                            fg=fg_color)
        address_label.grid(row=3, column=0, sticky=tk.E)

        person_address= tk.Label(frame_data,              #name
                            text = "Yliopistonkatu 4, 00100 Helsinki, Finland",
                            fg=fg_color)
        person_address.grid(row=3, column=1, sticky=tk.W)


        # Button that lets the user take a snapshot
        self.btn_snapshot=tk.Button(window, text="Snapshot", width=50, command=self.snapshot)
        self.btn_snapshot.grid(row=1, column=0)
        




        #Toggle Label
        # toggle_label= tk.Label(window,
        #     text = "The Switch Is On!",
        #     fg = "green",
        #     font = ("Helvetica", 32))
        # toggle_label.grid(row=1, column=1)


        # testG = tk.Label(window, text="Green", bg="green", fg="white")
        # testG.grid(row=1, column=1)
        # testP = tk.Label(window, text="Purple", bg="purple", fg="white")
        # testP.grid(row=2, column=1)


        #TODO - button to switch from inputted media to video capture



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
            #TODO - add rectangle with overlay



            # Convert the image back to a PhotoImage object
            self.photo = Image.fromarray(image)
            self.photo = ImageTk.PhotoImage(image=self.photo)

            # Display the image on the canvas
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        #After processing and delay, update image
        self.window.after(self.delay, self.update)



# Create a window and pass it to the Application object
camera(tk.Tk(), "Scorpion")

