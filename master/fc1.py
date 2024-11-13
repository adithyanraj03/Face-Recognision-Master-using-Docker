import cv2
import os
import matplotlib.pyplot as plt
import subprocess
import msvcrt

def take_screenshot():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Display the frame using matplotlib
        plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        plt.axis('off')
        plt.show()

        # Check if the space key is pressed
        if msvcrt.kbhit() and msvcrt.getch() == b' ':
            # Save the screenshot to a file
            screenshot_filename = 'temp/screenshot.png'
            cv2.imwrite(screenshot_filename, frame)
            print(f"Screenshot saved as '{screenshot_filename}'")

            # Execute main.py
            subprocess.call(["python", "main.py"])

            # Quit the code
            break

        # Check for 'q' key press to quit
        if msvcrt.kbhit() and msvcrt.getch() == b'q':
            break

    # Release the webcam and close the window
    cap.release()

def compare_images():
    # Load the captured image
    captured_image = cv2.imread('temp/screenshot.png')

    # Load the images from the "data" folder
    data_folder = 'data'
    for filename in os.listdir(data_folder):
        if filename.endswith('.jpg'):
            image_path = os.path.join(data_folder, filename)
            image = cv2.imread(image_path)

            # Perform facial recognition
            # Compare the captured image with the images in the "data" folder
            # Add your facial recognition code here

            # Display the result using matplotlib
            plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            plt.axis('off')
            plt.show()

if __name__ == "__main__":
    take_screenshot()
    compare_images()