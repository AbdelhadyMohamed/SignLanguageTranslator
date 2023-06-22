import tkinter as tk
from tkinter import ttk
import cv2
from PIL import Image, ImageTk
import threading
import os


class EnglishDictionaryPhrases:
    def __init__(self, root):
        self.root = root
        self.root.title("Sign Language Dictionary")
        self.root.config(bg='#7fcdcd')
        self.root.geometry("650x600+500+60")
        # Create the main frame
        main_frame = tk.Frame(self.root, bg="#7fcdcd")
        main_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        # Create a canvas to hold the video rows
        canvas = tk.Canvas(main_frame, bg="#7fcdcd")
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a scrollbar
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the canvas to use the scrollbar
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Create a frame inside the canvas to hold the video rows
        video_frame = tk.Frame(canvas, bg="#7fcdcd")
        canvas.create_window((0, 0), window=video_frame, anchor="nw")

        # Define the list of videos and label names
        video_folder = "Final ASL Phrases"
        videos = os.listdir(video_folder)

        # Load and display the videos
        num_videos_per_row = 3
        num_rows = (len(videos) + num_videos_per_row - 1) // num_videos_per_row

        back_button = tk.Button(self.root, text="Back", bg='white', font='android 20', fg='#0091E8')
        back_button.config(width=7, height=1)
        back_button.config(command=self.back_button_clicked)
        back_button.pack()

        for i in range(num_rows):
            row_frame = tk.Frame(video_frame, bg="#7fcdcd")
            row_frame.pack(side=tk.TOP, pady=10)

            for j in range(num_videos_per_row):
                index = i * num_videos_per_row + j

                if index < len(videos):
                    video_name = videos[index]
                    video_path = os.path.join(video_folder, video_name)

                    self.display_video(row_frame, video_path, video_name, i, j)

    def back_button_clicked(self):
        self.root.destroy()
        from MainApp import DictionaryEnglishWindow
        DictionaryEnglishWindow()

    def display_video(self, video_frame, video_path, video_name, row, column):
        # Create a label to hold the video
        video_label = tk.Label(video_frame, bg="#000000")
        video_label.grid(row=row, column=column, padx=10, pady=10)

        # Load the video
        video = cv2.VideoCapture(video_path)

        # Check if the video was loaded successfully
        if not video.isOpened():
            print(f"Failed to open video: {video_path}")
            return

        # Read the first frame of the video
        success, frame = video.read()

        # Check if the frame was read successfully
        if not success:
            print(f"Failed to read frame: {video_path}")
            return

        # Convert frame from BGR to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Resize frame while maintaining aspect ratio
        height, width, _ = frame_rgb.shape
        new_height = 280
        new_width = int(width * (new_height / height))
        frame_resized = cv2.resize(frame_rgb, (new_width, new_height))

        # Convert the resized frame to ImageTk format
        image = Image.fromarray(frame_resized)
        image_tk = ImageTk.PhotoImage(image)

        # Display the video frame
        video_label.configure(image=image_tk)
        video_label.image = image_tk

        # Create a play button for the video
        play_button = ttk.Button(video_frame, text="Play", command=lambda: self.play_video(video_path, video_label))
        play_button.grid(row=row+1, column=column, pady=5)

        # Create a label for the video name
        label = tk.Label(video_frame, text=video_name.split(".")[0])
        label.grid(row=row+2, column=column, pady=5)

    def play_video(self, video_path, video_label):
        # Create a new thread to play the video
        thread = threading.Thread(target=self._play_video_thread, args=(video_path, video_label))
        thread.start()


    def _play_video_thread(self, video_path, video_label):
        # Open the video file
        video = cv2.VideoCapture(video_path)

        # Check if the video was opened successfully
        if not video.isOpened():
            print(f"Failed to open video: {video_path}")
            return

        while True:
            # Read a frame from the video
            success, frame = video.read()

            # Check if the frame was read successfully
            if not success:
                break

            # Convert frame from BGR to RGB
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Resize frame while maintaining aspect ratio
            height, width, _ = frame_rgb.shape
            new_height = 280
            new_width = int(width * (new_height / height))
            frame_resized = cv2.resize(frame_rgb, (new_width, new_height))


            # Convert the resized frame to ImageTk format
            image = Image.fromarray(frame_resized)
            image_tk = ImageTk.PhotoImage(image)

            # Display the frame in the video label
            video_label.configure(image=image_tk)
            video_label.image = image_tk

            # Update the video label
            self.root.update_idletasks()
            self.root.update()

        # Release the video capture
        video.release()
