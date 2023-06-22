import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class ArabicSignLanguageDictionary:

    def __init__(self, root):
        self.root = root
        self.root.title("Sign Language Dictionary")
        self.root.config(bg='#7fcdcd')
        self.root.geometry("650x600+500+60")
        # Create the main frame
        main_frame = tk.Frame(self.root, bg="#7fcdcd")
        main_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        # Create a canvas to hold the image rows
        canvas = tk.Canvas(main_frame, bg="#7fcdcd")
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a scrollbar
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the canvas to use the scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Create a frame inside the canvas to hold the image rows
        image_frame = tk.Frame(canvas, bg="#7fcdcd")
        canvas.create_window((0, 0), window=image_frame, anchor="nw")

        # Define the list of image paths and letter names in the desired order
        image_paths = [
            "Arabic Avatars Final V/Arabic Avatars Final V/ا.png", "Arabic Avatars Final V/Arabic Avatars Final V/ب.png",
            "Arabic Avatars Final V/Arabic Avatars Final V/ت.png",
            "Arabic Avatars Final V/Arabic Avatars Final V/ث.png",
            "Arabic Avatars Final V/Arabic Avatars Final V/ج.png",
            "Arabic Avatars Final V/Arabic Avatars Final V/ح.png",
            "Arabic Avatars Final V/Arabic Avatars Final V/خ.png",
            "Arabic Avatars Final V/Arabic Avatars Final V/د.png",
            "Arabic Avatars Final V/Arabic Avatars Final V/ذ.png",
            "Arabic Avatars Final V/Arabic Avatars Final V/ر.png",
            "Arabic Avatars Final V/Arabic Avatars Final V/ز.png",
            "Arabic Avatars Final V/Arabic Avatars Final V/س.png",
            "Arabic Avatars Final V/Arabic Avatars Final V/ش.png",
            "Arabic Avatars Final V/Arabic Avatars Final V/ص.png",
            "Arabic Avatars Final V/Arabic Avatars Final V/ض.png",
            "Arabic Avatars Final V/Arabic Avatars Final V/ط.png",
            "Arabic Avatars Final V/Arabic Avatars Final V/ظ.png",
            "Arabic Avatars Final V/Arabic Avatars Final V/ع.png",
            "Arabic Avatars Final V/Arabic Avatars Final V/غ.png",
            "Arabic Avatars Final V/Arabic Avatars Final V/ف.png",
            "Arabic Avatars Final V/Arabic Avatars Final V/ق.png",
            "Arabic Avatars Final V/Arabic Avatars Final V/ك.png",
            "Arabic Avatars Final V/Arabic Avatars Final V/ل.png",
            "Arabic Avatars Final V/Arabic Avatars Final V/م.png",
            "Arabic Avatars Final V/Arabic Avatars Final V/ن.png",
            "Arabic Avatars Final V/Arabic Avatars Final V/ه.png",
            "Arabic Avatars Final V/Arabic Avatars Final V/و.png",
            "Arabic Avatars Final V/Arabic Avatars Final V/ي.png",
            # Add more image paths here
        ]
        letter_names = [
            "ا", "ب", "ت", "ث", "ج", "ح", "خ", "د", "ذ", "ر", "ز", "س", "ش", "ص", "ض", "ط", "ظ", "ع", "غ",
            "ف", "ق", "ك", "ل", "م", "ن", "ه", "و", "ي"
        ]

        # Create image rows
        row_size = 3  # Number of images in each row
        num_rows = (len(image_paths) + row_size - 1) // row_size  # Calculate number of rows

        for i in range(num_rows - 1):
            image_row_frame = tk.Frame(image_frame, bg="#7fcdcd")
            image_row_frame.pack(side=tk.TOP, padx=10, pady=10)

            # Iterate over images in the row in reverse order
            for j in range(i * row_size + row_size - 1, i * row_size - 1, -1):
                image_path = image_paths[j]
                letter_name = letter_names[j]

                # Create a frame to hold image and label
                image_label_frame = tk.Frame(image_row_frame, bg="#7fcdcd")
                image_label_frame.pack(side=tk.LEFT)

                # Load and display the image
                image = Image.open(image_path)
                image = image.resize((200, 200), Image.ANTIALIAS)
                image_tk = ImageTk.PhotoImage(image=image)

                # Create an image label
                image_label = tk.Label(image_label_frame, bg="white", image=image_tk)
                image_label.pack()

                # Create a label for the letter name below the image with bold font
                letter_label = tk.Label(image_label_frame, text=letter_name, font="bold")
                letter_label.pack()

                # Store reference to the image
                image_label.image = image_tk

        # Create a separate row for the last letter "ي"
        last_row_frame = tk.Frame(image_frame, bg="#7fcdcd")
        last_row_frame.pack(side=tk.TOP, padx=10, pady=10)

        # Load and display the image for "ي"
        last_image_path = image_paths[-1]
        last_letter_name = letter_names[-1]
        last_image = Image.open(last_image_path)
        last_image = last_image.resize((200, 200), Image.ANTIALIAS)
        last_image_tk = ImageTk.PhotoImage(image=last_image)

        # Create an image label for "ي"
        last_image_label = tk.Label(last_row_frame, bg="white", image=last_image_tk)
        last_image_label.pack()

        # Create a label for the letter name below the image with bold font for "ي"
        last_letter_label = tk.Label(last_row_frame, text=last_letter_name, font="bold")
        last_letter_label.pack()

        # Store reference to the image
        last_image_label.image = last_image_tk

        back_button = tk.Button(self.root, text="Back", bg='white', font='android 20', fg='#0091E8')
        back_button.config(width=10, height=1)
        back_button.config(command=self.back_button_clicked)
        back_button.pack()

    def back_button_clicked(self):
        self.root.destroy()
        from MainApp import ArabicWindow
        ArabicWindow()
