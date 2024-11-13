import cv2
import keyboard
from matplotlib import pyplot as plt

def take_screenshot():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Convert the frame to RGB format
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Display the frame using matplotlib
        plt.imshow(frame_rgb)
        plt.axis('off')
        plt.show()

        # Check if the space key is pressed
        if keyboard.is_pressed('space'):
            # Save the screenshot to a file
            screenshot_filename = 'screenshot.png'
            cv2.imwrite(screenshot_filename, frame)
            print(f"Screenshot saved as '{screenshot_filename}'")
            break

        # Check for 'q' key press to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam
    cap.release()

if __name__ == "__main__":
    take_screenshot()