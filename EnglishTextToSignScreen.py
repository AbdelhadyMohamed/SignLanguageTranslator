import os
import cv2
import tkinter as tk
from PIL import ImageTk, Image

class EnglishTextToSignScreen():

    def __init__(self):
        # Set the path to your video folder
        self.VIDEO_FOLDER = "Handtalk Letters MP4"
        self.root = tk.Tk()
        self.root.title("Text to Sign")
        self.root.geometry("650x600+500+60")
        #root.overrideredirect(True)

        # Create the main frame
        main_frame = tk.Frame(self.root)
        
        main_frame.pack(expand=True, fill=tk.BOTH)
        main_frame.config(bg='#e7e5e8')

        # Create the video player frame
        self.video_frame = tk.Frame(main_frame, width=405, height=410)
        self.video_frame.pack(side=tk.TOP, pady=20)
        self.video_frame.config(bg='#e7e5e8')
        self.video_label = tk.Label(self.video_frame)
        self.video_label.pack(expand=True, fill=tk.BOTH)
        self.video_label.config(bg='#e7e5e8')

        # Create the letter entry frame
        self.letter_frame = tk.Frame(main_frame, pady=20)
        self.letter_frame.pack(side=tk.BOTTOM, padx=20, pady=30)

        self.letter_label = tk.Label(self.letter_frame, text="Enter a letter:")
        self.letter_label.pack(side=tk.LEFT)

        self.letter_entry = tk.Entry(self.letter_frame)
        self.letter_entry.pack(side=tk.LEFT, padx=10)

        self.play_button = tk.Button(self.letter_frame, text="Go", command=self.play_video)
        self.play_button.pack(side=tk.LEFT)

        #self.repeat_button = tk.Button(self.letter_frame, text="Repeat Video", command=self.repeat_video, state=tk.DISABLED)
        #self.repeat_button.pack(side=tk.LEFT, padx=10)

        self.back_button = tk.Button(self.letter_frame, text="Back", command=self.Back)
        self.back_button.pack(side=tk.LEFT, padx=10)

        self.no_video_label = tk.Label(main_frame, fg="red")
        self.no_video_label.pack(side=tk.BOTTOM)
        self.root.mainloop()

    def play_video(self):
        # Get the input text from the letter entry
        text = self.letter_entry.get()


        # Check if the input is a single letter or a word
        if len(text) == 1:
            # If the input is a single letter, play the corresponding video
            letter = text.upper()
            video_file = os.path.join(self.VIDEO_FOLDER, f"{letter}.mp4")
            if os.path.exists(video_file):
                self.no_video_label.pack_forget()  # Hide the label if it was previously shown
                cap = cv2.VideoCapture(video_file)
                while True:
                    ret, frame = cap.read()
                    if not ret:
                        break
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    frame = cv2.resize(frame, (405, 410))
                    frame = Image.fromarray(frame)
                    frame = ImageTk.PhotoImage(frame)
                    self.video_label.configure(image=frame)
                    self.video_label.image = frame
                    self.root.update()
                    cv2.waitKey(1)  # Delay to display each frame
                cap.release()
                #letter_entry.delete(0, tk.END)  # Clear the text bar after the video is played
                #self.repeat_button.config(state=tk.NORMAL)  # Enable the 'Repeat' button after the video is played
            else:
                self.no_video_label.configure(text=f"No video found for letter '{letter}'")
                self.no_video_label.pack(side=tk.BOTTOM)

        else:
            # If the input is a word, play the videos for each letter in sequence
            for letter in text.upper():
                video_file = os.path.join(self.VIDEO_FOLDER, f"{letter}.mp4")
                if os.path.exists(video_file):
                    self.no_video_label.pack_forget()  # Hide the label if it was previously shown
                    cap = cv2.VideoCapture(video_file)
                    while True:
                        ret, frame = cap.read()
                        if not ret:
                            break
                        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        frame = cv2.resize(frame, (405, 410))
                        frame = Image.fromarray(frame)
                        frame = ImageTk.PhotoImage(frame)
                        self.video_label.configure(image=frame)
                        self.video_label.image = frame
                        self.root.update()
                        cv2.waitKey(16)  # Delay to display each frame
                    cap.release()
                    #letter_entry.delete(0, tk.END)  # Clear the text bar after the video is played


    # Define the function to repeat the video
    def repeat_video(self):
        letter = self.letter_entry.get()
        video_file = os.path.join(self.VIDEO_FOLDER, f"{letter}.mp4")
        if os.path.exists(video_file):
            cap = cv2.VideoCapture(video_file)
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = cv2.resize(frame, (405, 410))
                frame = Image.fromarray(frame)
                frame = ImageTk.PhotoImage(frame)
                self.video_label.configure(image=frame)
                self.video_label.image = frame
                self.root.update()
                cv2.waitKey(1)  # Delay to display each frame
            cap.release()
        else:
            self.no_video_label.configure(text=f"No video found for letter '{letter}'")
            self.no_video_label.pack(side=tk.BOTTOM)
    def Back(self):
        self.root.destroy()
        from MainApp import TranslationEnglishWindow
        TranslationEnglishWindow()
