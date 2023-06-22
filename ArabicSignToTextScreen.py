import cv2
import numpy as np
import time
import arabic_reshaper
from bidi.algorithm import get_display
from tensorflow.keras.models import load_model
import keyboard

from PIL import ImageFont, ImageDraw, Image


class ArabicSignToTextScreen:

    def __init__(self):
        # Load the trained model
        model = load_model('ArabModel.h5')
        model.summary()

        # Set the video capture device (webcam)
        cap = cv2.VideoCapture(0)
        classes = ['ع', 'ال', 'ا', 'ب', 'د', 'ظ', 'ض', 'ف',
                   'ق', 'غ', 'ه', 'ح', 'ج', 'ك', 'خ',
                   'لا', 'ل', 'م', 'ن', 'ر', 'ص', 'س',
                   'ش', 'ط', 'ت',
                   'ث', 'ذ', 'ة', 'و', 'ئ', 'ي', 'ز']

        # Initialize variables
        stable_prediction = ''
        prediction_stable_for = 0
        last_prediction_time = 0
        string = ''

        while True:

            # Capture frame-by-frame
            ret, frame = cap.read()

            # Check if the spacebar key has been pressed
            key = cv2.waitKey(1) & 0xFF
            if key == ord(' '):
                string += ' '

            # Convert the frame to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Crop the region of interest (ROI)
            roi = gray[100:300, 100:300]

            # Resize the ROI to (64, 64)
            img = cv2.resize(roi, (64, 64))
            img = img / 255.0

            # Convert the image to a 4D array (batch_size, height, width, channels)
            img = np.reshape(img, (1, 64, 64, 1))

            # Make a prediction
            prediction = model.predict(img)
            index = np.argmax(prediction)
            letter = classes[index]
            accuracy = prediction[0][index]

            # Print the predicted class
            predicted_class = classes[np.argmax(prediction)]
            reshaped_predicted_letter = arabic_reshaper.reshape('الحرف المتوقع: ' + predicted_class)
            display_predicted_letter = get_display(reshaped_predicted_letter)
            print("Predicted class:", display_predicted_letter)

            # Check if the prediction is stable for 3 seconds
            current_time = time.time()
            if predicted_class == stable_prediction:
                prediction_stable_for = (current_time - last_prediction_time)
                timer = round(3 - prediction_stable_for, 2)
            else:
                stable_prediction = predicted_class
                prediction_stable_for = 0
                last_prediction_time = current_time

            if prediction_stable_for >= 3:
                string += predicted_class
                stable_prediction = ''
                prediction_stable_for = 0

            # Check if backspace key is pressed
            # Check if backspace key is pressed
            if keyboard.is_pressed('backspace'):
                if len(string) > 0:
                    string = string[:-1]
            elif keyboard.is_pressed('q'):
                break

            # Draw a rectangle around the ROI
            cv2.rectangle(frame, (100, 100), (300, 300), (0, 255, 0), 2)

            # Convert the frame to RGB for Pillow
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_frame = Image.fromarray(frame_rgb)

            # Choose a font (adjust the path to your font file)
            font_path = "arial.ttf"
            font = ImageFont.truetype(font_path, 40)

            # Create a Pillow ImageDraw object to draw text
            draw = ImageDraw.Draw(pil_frame)

            # Reshape and align the Arabic text for word
            reshaped_word = arabic_reshaper.reshape('الكلمة: ' + string)
            display_word = get_display(reshaped_word)
            draw.text((20, 20), display_word, font=font, fill=(255, 255, 255))

            # Reshape and align the Arabic text for predicted letter
            reshaped_predicted_letter = arabic_reshaper.reshape('الحرف المتوقع: ' + predicted_class)
            display_predicted_letter = get_display(reshaped_predicted_letter)
            draw.text((20, 80), display_predicted_letter, font=font, fill=(255, 0, 0))

            # Reshape and align the Arabic text for accuracy
            reshaped_accuracy = arabic_reshaper.reshape('الدقة: ' + str(round(accuracy * 100, 2)) + '%')
            display_accuracy = get_display(reshaped_accuracy)
            draw.text((20, 140), display_accuracy, font=font, fill=(0, 255, 0))

            # Convert the Pillow image back to BGR for OpenCV
            frame_bgr = cv2.cvtColor(np.array(pil_frame), cv2.COLOR_RGB2BGR)

            # Display the frame
            cv2.imshow('Sign to Text', frame_bgr)

        # Release the capture device and close all windows
        cap.release()
        cv2.destroyAllWindows()
