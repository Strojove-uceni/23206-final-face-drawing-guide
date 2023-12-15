**Face Drawing Guide**

This project aspire to create an AI tool for art beginners. The goal is to help "art babies" see the guidlines and shapes in faces which can help them to learn how to draw a face on their own.

The main goal is to divide a face in an uploaded photography into simple shapes. We chose to focus on drawing a circle to represent cranium and an ellipse as a chin. This division is supossed to help sketching the main structure of the face and strenghten the mental library of the artist to draw faces without reference in future if they wish to.

We decided to use a self-constructed dense neural network (NN). The goal was to train a NN which would detect the radius and center coordinates of a circle and ellipse which would best approximate the given face. MediaPipe was later utilized in the training process which resulted in a better performance of the network.

Our project introduces a fully functioning, MedaiPipe dependent neural network approach to face drawing.

<img src="Img/01.png" width="400">

