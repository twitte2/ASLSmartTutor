#run python asl.py
#gesture in the frame of roi
#to exit, hit space

from tkinter import Scale
from keras.models import load_model
import cv2
import numpy as np

from random import choice

#pip install flask
from socket import SocketIO
from flask import Flask, request, jsonify, Response
from flask import Flask, request, render_template
from flask_cors import CORS
import base64

app = Flask(__name__)
# socket = SocketIO(app, cors_allowed_origins = "*")
CORS(app)


REV_CLASS_MAP = {
   0: "a",
   1: "b",
   2: "c",
   3: "d",
   4: "e",
   5: "f",
   6: "g",
   7: "h",
   8: "i",
   9: "j",
   10: "k",
   11: "l",
   12: "m",
   13: "n",
   14: "o",
   15: "p",
   16: "q",
   17: "r",
   18: "s",
   19: "t",
   20: "u",
   21: "v",
   22: "w",
   23: "x",
   24: "y",
   25: "z",
   26: "nothing"
}
def mapper(val):
    return REV_CLASS_MAP[val]
def calculate_winner(user_move):
    if user_move == "a":
        return "A"
    elif user_move == "b":
        return "B" 
    elif user_move == "c":
        return "C"
    elif user_move == "d":
        return "D"
    elif user_move == "e":
        return "E"
    elif user_move == "f":
        return "F"
    elif user_move == "g":
        return "G"
    elif user_move == "h":
        return "H"
    elif user_move == "i":
        return "I"
    elif user_move == "j":
        return "J"
    elif user_move == "k":
        return "K"
    elif user_move == "l":
        return "L"
    elif user_move == "m":
        return "M"
    elif user_move == "n":
        return "N"
    elif user_move == "o":
        return "O"
    elif user_move == "p":
        return "P"
    elif user_move == "q":
        return "Q"
    elif user_move == "r":
        return "R"
    elif user_move == "s":
        return "S"
    elif user_move == "t":
        return "T"
    elif user_move == "u":
        return "U"
    elif user_move == "v":
        return "V"
    elif user_move == "w":
        return "W"
    elif user_move == "x":
        return "X"
    elif user_move == "y":
        return "Y"
    elif user_move == "z":
        return "Z"
    elif user_move == "nothing":
        return "nothing"

model = load_model("game-model.h5")
cap = cv2.VideoCapture(0)

def imageguess():
    file = cv2.imread("imageToSave.png")
    img = cv2.cvtColor(file, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (227, 227))
    img = cv2.flip(img, 1)
    # predict the move made
    pred = model.predict(np.array([img]))
    move_code = np.argmax(pred[0])
    user_move_name = mapper(move_code)
    return user_move_name

@app.route('/')
def index():
    return render_template('index.html')

#@socket.on('message')
@app.route('/uploadImage/', methods=['POST'])
def upload_base64_file():
    data = request.get_json()
    if data is None:
        print("No valid request body, json missing!")
        return jsonify({'error': 'No valid request body, json missing!'})
    else:
        img_data = data['image']
        header, img_data = img_data.split(",", 1)
        with open("imageToSave.png", "wb") as fh:
            #saving the image
            #base64.b64decode(img_data + '==') 
            #above line is the image. if needed, call this in place of an image for the functions
            fh.write(base64.b64decode(img_data + '=='))


        response = imageguess()
        print(response)
        return Response("{\"results\":\"" + response + "\"}", status=201, mimetype='application/json')


if __name__ == '__main__':
    app.run(host="localhost", port=80, debug=True)



# while True:
#     ret, frame = cap.read()
#     frame = cv2.flip(frame,1)
#     if not ret:
#         continue
#     #cv2.rectangle(frame, (10, 300), (310, 630), (0, 255, 0), 2)
#     cv2.rectangle(frame, (910, 300), (1210, 600), (0, 0, 0), 2)
    
#     # extract the region of image within the user rectangle
#     #roi = frame[300:630, 10:310]
#     roi = frame[300:600, 910:1210]
#     img = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
#     img = cv2.resize(img, (227, 227))
#     # predict the move made
#     pred = model.predict(np.array([img]))
#     move_code = np.argmax(pred[0])
#     user_move_name = mapper(move_code)
    
#     font = cv2.FONT_HERSHEY_SIMPLEX
#     cv2.putText(frame, "Your Move: " + user_move_name,
#                 (10, 50), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
    
#     cv2.imshow("ASL Smart Tutor", frame)
#     k = cv2.waitKey(10)
#     if k == ord(' '):
#         break
# cap.release()
# cv2.destroyAllWindows()