import ctypes
import tkinter as tk
from MainApp import StartWindow
from PIL import Image, ImageTk

class AppStart:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Let's Sign")
        # Set the path to your ICO file
        icon_path = "icon.ico"
        # Load the icon using ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
        self.root.iconbitmap(default=icon_path)
        self.root.geometry("+0+0")
        self.root.config(bg='#7fcdcd')
        self.root.iconbitmap("icon.ico")
        self.root.minsize(1350, 690)
        self.root.maxsize(1300, 530)

        # Create the labels for the text
        label1 = tk.Label(self.root, text='Welcome to ', bg='#7fcdcd', fg='#FFFFFF',
                         font=('AR BLANCA', 40))
        label1.place(x=140, y=180)

        label2 = tk.Label(self.root, text='Let’s Sign', bg='#7fcdcd', fg='#FFFFFF',
                          font=('AR BLANCA', 60, 'bold'))
        label2.place(x=140, y=250)

        label3 = tk.Label(self.root, text='A Two-way Sign Language Translator that breaks  ',
                          bg='#7fcdcd', fg='#FFFFFF',
                          font=('Chaparral Pro Light', 20, 'bold'))
        label3.place(x=140, y=380)

        label4 = tk.Label(self.root, text='barriers between Deaf & Normal People.',
                          bg='#7fcdcd', fg='#FFFFFF',
                          font=('Chaparral Pro Light', 20, 'bold'))
        label4.place(x=140, y=420)

        # Create the "Let’s Start" button
        start_button = tk.Button(self.root, text="Let’s Start", bg='white', font='android 20')
        start_button.config(width=8, height=1)
        start_button.config(command=self.start_button_clicked)
        start_button.place(x=280, y=500)

        # Load the image and create a PhotoImage object
        image = Image.open("start.png")
        image = image.resize((500, 500))  # Resize the image as per your requirements
        photo = ImageTk.PhotoImage(image)

        # Create a label to display the image
        image_label = tk.Label(self.root, image=photo, bg='white')
        image_label.place(x=800, y=90)

        self.root.mainloop()

    def start_button_clicked(self):
        self.root.destroy()
        StartWindow()

run_app = AppStart()
run_app
