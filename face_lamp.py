# Import necessary modules
from requests import post
from requests.exceptions import ConnectionError
from requests.exceptions import ConnectTimeout
from time import sleep
from time import time
import cv2

video_capture = cv2.VideoCapture(0)


# Sends an HTTP POST request to server.py (Open the README.md to find a link to my step-by-step tutorial in which I expain how to use this program
def change_lamp_state(state):
    payload = {
            'command': 'DeskLamp',
            'state': str(int(bool(state)))
    }

    try:
        post('http://<ip_address>:5000/command', data=payload)
    except ConnectionError:
        print('requests.exceptions.ConnectionError')
    except:
        print('requests.exceptions.ConnectTimeout')


cascPath = 'haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascPath)


# Check if the program is enabled. If it is not the change_lamp_state function will not be called.
# kestroke.py waits for a keystroke to toggle the state of the program. Keystroke: ctrl+alt+x
def auto_enabled():
    auto_file = open('auto.txt', 'rt')
    file_contents = auto_file.read()
    auto_file.close()

    if file_contents == 'OFF':
        auto = False
    elif file_contents == 'ON':
        return True



timestamp = -1
while True:
    sleep(0.6)

    # Capture video in order to detect faces
    ret, frame = video_capture.read()

    # Modify the frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    print(faces)

    # Controls the light
    # 20 is how much time would it take the light to turn off after the program doesn't see any other faces
    if len(faces) > 0:
         timestamp = time()

    if time() - timestamp <= 20:
        if auto_enabled():
            change_lamp_state(True)
    else:
        if auto_enabled():
            change_lamp_state(False)

# Stop capturing video
video_capture.release()
