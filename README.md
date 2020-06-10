<center><h1>OpenCV-Sudoku-Solver</h1>
<img src="assets\FrontPoster.jpg" alt="drawing" width="256" height="256"/><img src="assets\BacksidePoster.jpg" alt="drawing" width="256" height="256"/></center>

# INSPIRATION
Well, I'm not a good Sudoku player, generally hesitate to solve a sudoku. Also it's quite time consuming. One day i came to know about Artificial Intelligence and how it can be used to replicate humans work. I got very facinated by the fact that i can teach my machine to solve a sudoku that can solve quite faster and efficiently than even i could do. Exploring my excitement, I build this OpenCV Sudoku Solver that takes picture of a sudoku as an input and displays a solved sudoku within a minute
# Folder Structure
```
SUDOKU
│   README.md
│   LICENCE    
│   app.py
│   .gitignore
│   .gitattributes
└───templates
│   │   index.html
│   
└───static
│   │
│   └───css
│   │   │   mainpage.css 
│   │
│   └───img
│   │   │   background.jpg
│   │
│   └───upload
│
└───src
│   │
│   └───digit detection
│   │   │
│   │   └───digits
│   │   │   │
│   │   │   └───1
│   │   │   │
│   │   │   └───2
│   │   │   │   ..
│   │   │   │   ..
│   │   │   └───9
│   │   │
│   │   └───pickle files
│   │   │   │   X.pickle
│   │   │   │   Y.pickle
│   │   │
│   │   │   create_dataset.py
│   │   │   model_training.py
│   │
│   │   AR.py
│   │   digitExtractor.py
│   │   gridExtractor.py
│   │   helper.py
│   │   model_path.py
│   │   recognizeDigit.py
│   │   solver.py   
│
└───model
│   │   Model.h5
└───input
│
└───example
│   |   sudoku.jpg
│
└───assets
│   │   BacksidePoster.jpg
│   │   FrontPoster.jpg
```
# File Description
> * app .py => Our Flask framework
> * templates => Contains our Frontend Files
> * static => Contains Static Files for Flask
> * src => Backend or the Main Logic of our app
> * model => Trained Model to be used for Prediction
> * input => Stores the Image passed by User
> * example => Sample of picture for Testing Purpose
> * assets => Files required for README .md

# How App Works
1. Photo containing received via frontend sent to flask server in base64 form.
2. After decoding, image saved in **input** folder which is further picked up by backend.
3. **gridExtractor .py** picks the image, finds the Sudoku Grid by finding the biggest rectangle in Image. Region of Interest is cropped out and sent as input to **digitExtrator .py**
4. **digitExtractor .py** crop out each cell of Sudoku and runs **recognizeDigit .py** that recognize Digit with the help of a trained Model trained in **digit detection** directory, path saved in **model_path .py**
5. Detected Digits saved in a array passed to **solver .py** that solves the Sudoku via Backtracking.
6. Solution produced by **solver .py** passed to **AR .py** where missing values are printed over Image. Resultant Image and Image highlighting Cropped Section from step 3 saved in **static/upload** folder.
7. Later **static/upload** referred to get Results to be displayed back to frontend

# Landing Page
<img src="assets\landingPage.png" alt="drawing" width="100%" height="400"/>

# Input 
<img src="assets\input.png" alt="drawing" width="100%" height="400"/>

# Loading Screen 
<img src="assets\loadingScreen.png" alt="drawing" width="100%" height="400"/>

# Output Screen 
<img src="assets\outputScreen.png" alt="drawing" width="100%" height="400"/>

# Required Libraries
* numpy==1.18.1
* opencv_python==4.1.2.30
* Keras==2.3.1
* Flask==1.1.2

# How to Use?
Clone the Repository and run app .py
> python app .py

And You're Good to Go

# Drawbacks
1. This App is based on an assumption that biggest rectangle in the image corrosponds to Sudoku Grid.
In Other Scenario, App fails
>Fails to extract Sudoku Grid perfectly
<img src="assets\failedImg.jpg" alt="drawing" width="100%" height="400"/>

2. Our Model is trained on a small dataset. Therefore, underperforms against few Sudoku
>Here, Grid is properly extracted but failed to recognize all digits correctly 
<img src="assets\notRecognized.jpg" alt="drawing" width="100%" height="400"/>

# Retrain Existing Model
Unfortunately, I haven't a clear pipeline for retraining of existing Model. But You can follow these steps :

1. Uncomment lines 55-57 in **gridExtractor .py** and pass a Sudoku Image inorder to extract Sudoku Grid.
2. Uncomment line 49 and line 66 from **digitExtractor .py** and pass the Sudoku Grid. This will save each cell of the Sudoku as an image in the given folder.
3. Remove image with no digit. Manually segregate the digits and move them to respective directory in **digit detection\digits**
4. Run **digit detection\create_dataset .py** to create pickle files of train images and labels
5. Run **model_training .py** and wait for your model to get trained

# To-Do(s)
1. Exception handling (Currently frontend doesn't react when any of Drawback occurs)
2. Displaying Remaining Times (Approx 1.5mins-2mins taken to complete the process)
3. Optimize Frontend for not Desktop Setups
4. Clean Pipeline for Retraining

> Note: Please don't send PR just to remove comments. Havn't removed them for a reason :)
