import os
import tkinter as tk
from PIL import ImageTk, Image

class ArabicTextToSignScreen():

    def __init__(self):
        # Set the path to your image folder
        self.IMAGE_FOLDER = "Arabic Avatars Final V/Arabic Avatars Final V"
        self.root = tk.Tk()
        self.root.title("Text to Sign")
        self.root.geometry("650x600+500+60")

        # Create the main frame
        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True, fill=tk.BOTH)
        main_frame.config(bg='#e7e5e8')

        # Create the image display frame
        self.image_frame = tk.Frame(main_frame, width=409, height=394)
        self.image_frame.pack(side=tk.TOP, pady=20)
        self.image_frame.config(bg='#e7e5e8')
        self.image_label = tk.Label(self.image_frame)
        self.image_label.pack(expand=True, fill=tk.BOTH)
        self.image_label.config(bg='#e7e5e8')

        # Create the letter entry frame
        self.letter_frame = tk.Frame(main_frame, pady=20)
        self.letter_frame.pack(side=tk.BOTTOM, padx=20, pady=30)

        self.letter_label = tk.Label(self.letter_frame, text="Enter a word:")
        self.letter_label.pack(side=tk.LEFT)

        self.letter_entry = tk.Entry(self.letter_frame)
        self.letter_entry.pack(side=tk.LEFT, padx=10)

        self.play_button = tk.Button(self.letter_frame, text="Go", command=self.play_images)
        self.play_button.pack(side=tk.LEFT)

        self.back_button = tk.Button(self.letter_frame, text="Back", command=self.back)
        self.back_button.pack(side=tk.LEFT, padx=10)

        self.no_image_label = tk.Label(main_frame, fg="red")
        self.no_image_label.pack(side=tk.BOTTOM)
        self.root.mainloop()

    def play_images(self):
        # Get the input text from the letter entry
        text = self.letter_entry.get()

        # Check if the input is not empty
        if text:
            self.no_image_label.pack_forget()  # Hide the label if it was previously shown

            # Clear the image label
            self.image_label.config(image=None)

            # Split the text into individual letters
            letters = list(text.upper())

            # Display the images with a delay
            self.display_images(letters)

    def display_images(self, letters):
        if letters:
            letter = letters.pop(0)

            # Check if the image exists for the current letter
            image_file = os.path.join(self.IMAGE_FOLDER, f"{letter}.png")
            if os.path.exists(image_file):
                image = Image.open(image_file)
                image = image.resize((409, 394), Image.ANTIALIAS)
                image = ImageTk.PhotoImage(image)
                self.image_label.configure(image=image)
                self.image_label.image = image

            # Schedule the display of the next image
            self.root.after(500, self.display_images, letters)

    def back(self):
        self.root.destroy()
        from MainApp import TranslationArabicWindow
        TranslationArabicWindow()
