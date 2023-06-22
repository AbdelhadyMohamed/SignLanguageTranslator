import cv2
import numpy as np
import time
from tensorflow.keras.models import load_model
import keyboard


class EnglishSignToTextScreen:
    def __init__(self):
        # Load the trained model
        self.model = load_model("newmodel22.h5")
        # Set the video capture device (webcam)
        self.cap = cv2.VideoCapture(0)

        self.cap.set(50, 30)
        self.classes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M',
                        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']

        # Initialize variables
        self.stable_prediction = ''
        self.prediction_stable_for = 0
        self.last_prediction_time = 0
        self.string = ''

        while True:
            # Capture frame-by-frame
            self.ret, frame = self.cap.read()
            # Check if the spacebar key has been pressed
            self.key = cv2.waitKey(1) & 0xFF
            if self.key == ord(' '):
                self.string += ' '
            # Convert the frame to grayscale
            self.gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Crop the region of interest (ROI)
            roi = self.gray[100:300, 100:300]

            # Resize the ROI to (32, 32)
            self.img = cv2.resize(roi, (28, 28))
            self.img = self.img / 255.0
            # Convert the image to RGB
            # self.img = cv2.cvtColor(self.img, cv2.COLOR_GRAY2RGB)

            # Reshape the image to (1, 32, 32, 3)
            self.img = np.reshape(self.img, (1, 28, 28, 1))

            # Make a prediction
            self.prediction = self.model.predict(self.img)
            self.index = np.argmax(self.prediction)
            letter = self.classes[self.index]
            self.accuracy = self.prediction[0][self.index]

            # Print the predicted class
            self.predicted_class = self.classes[np.argmax(self.prediction)]
            print("Predicted class:", self.predicted_class)

            # Check if the prediction is stable for 3 seconds
            current_time = time.time()
            if self.predicted_class == self.stable_prediction:
                prediction_stable_for = (current_time - self.last_prediction_time)
                self.timer = round(3 - prediction_stable_for, 2)
            else:
                self.stable_prediction = self.predicted_class
                prediction_stable_for = 0
                self.last_prediction_time = current_time

            if prediction_stable_for >= 3:
                self.string += self.predicted_class
                self.stable_prediction = ''
                self.prediction_stable_for = 0

            # Check if backspace key is pressed
            if keyboard.is_pressed('backspace'):
                if len(self.string) > 0:
                    self.string = self.string[:-1]
            elif keyboard.is_pressed('q'):
                break

            # Draw a rectangle around the ROI
            cv2.rectangle(frame, (100, 100), (300, 300), (0, 255, 0), 2)

            # Display the frame with the predicted class and string
            cv2.putText(frame, 'Predicted Letter: ' + str(self.predicted_class), (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
                        0.8, (0, 0, 255), 2)

            cv2.putText(frame, 'Accuracy: ' + ' (' + str(round(self.accuracy * 100, 2)) + '%)', (50, 80),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            cv2.putText(frame, 'Word: ' + self.string, (50, 360), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
            cv2.imshow('Sign to Text', frame)

            # Release the capture device and close all windows
        self.cap.release()
        cv2.destroyAllWindows()
