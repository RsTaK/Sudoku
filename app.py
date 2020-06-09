from flask import Flask, request, render_template, send_from_directory, make_response,jsonify
import cv2
import base64
import numpy as np
from src.gridExtractor import gridExtractor
from src.digitExtractor import digitExtractor
from src.solver import Sudoku_Solver
from src.AR import AR
from src import helper
import json

def decodebyte64(data,filename):
    string=data.split(",")[1]
    decoded=base64.b64decode(string)
    with open('input/'+filename, "wb") as f:
        f.write(decoded)

def build():
    img_path=r'input\default.jpg'
    #model=r'model\Model.h5'
    croppedImage=gridExtractor(img_path).output
    recognized_sudoku = digitExtractor(croppedImage).output
    solved_sudoku = Sudoku_Solver(recognized_sudoku).output
    AR(croppedImage, solved_sudoku)
    helper.destroyWindows()

app = Flask(__name__, static_url_path='/static/')
#app.config["UPLOAD_FOLDER"] = "/root_flask_app/static/upload/"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    names = request.get_json() 
    encoded_path = names["filepath"]
    decodebyte64(encoded_path,"default.jpg")
    #build()
    croppedImage='/static/upload/cropped_Image.jpg'
    solvedImage='/static/upload/solved_Image.jpg'


    return jsonify({"croppedImage":croppedImage,"solvedImage":solvedImage})

if __name__ == "__main__":
    app.run(debug=True)