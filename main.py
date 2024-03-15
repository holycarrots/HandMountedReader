'''
This Python script utilizes the OpenCV library to access the webcam and continuously capture 
frames. Within each iteration of the loop, the script uses Pytesseract, a Python wrapper for 
Google's Tesseract OCR engine, to extract text from the captured frame. If text is detected, it's 
spoken aloud using the pyttsx3 library, which initializes a text-to-speech engine. Additionally, the 
detected text is overlaid onto the frame using OpenCV's putText function to provide a visual 
representation of the recognized text. The program runs until the user presses the 'q' key to quit, 
at which point it releases the webcam and closes all windows. This script essentially creates a 
real-time text recognition and speech synthesis system, capable of processing live video feed 
from a webcam and audibly reading any detected text.'''


import pytesseract
import pyttsx3
import cv2 

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Path to the Tesseract OCR executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Open the webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # Read a frame from the webcam
    ret, frame = cap.read()

    if not ret:
        print("Unable to capture video.")
        break

    # Use Tesseract OCR to extract text from the image
    text = pytesseract.image_to_string(frame)

    # Check if any text was detected
    if text.strip():
        # Speak the detected text
        engine.say(text)
        engine.runAndWait()

    # Display the frame with the detected text
    cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow('Text Detection', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()