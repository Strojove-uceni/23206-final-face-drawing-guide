<img src="Img/01.png" width="400">

# **Face Drawing Guide**

This project aspires to create an AI tool inspired by Loomis method for art beginners. The goal is to help "art babies" see the guidlines and shapes in faces which can help them to learn how to draw a face on their own.

A functioning demonstration of the code is presented in the `Face_drawing_guide_demo.ipynb` notebook. This is the executable file of interest.

The *additional codes* folder then contains all files used for image annotation, facial lendmarking and dataset manipulations. They are briefly explaind in the following text:

  1. `FDG_anot.py` is used to interactively draw circles and images inside images and serves as a data annotator.
  2. `anot_test.py` shows the images with their annotations and exports them.
  3. `MediaPipe_landmarks.ipynb` finds facial landmarks in images. 
  4. `pipe.py` serves as a filtering code. It was used to filter the MediaPipe wrongly detected images out of the dataset.
  5. `modelFDG_checkpoint.ckpt` is the trained model.



