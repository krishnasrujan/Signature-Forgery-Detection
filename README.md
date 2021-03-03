# Signature-Forgery-Detection

# Objective
​ To create a model which detects signature forgery. It should work for unseen data as well. 

​ Deploy the model and use it in real time signature forgery detection.

# Siamese Network

Siamese Network is a one of it's kind architecture in which weights are shared between all inputs in one iteration. It is also called One Shot Learning as retraining of model is not required when new data arrives.

<img width="256" alt="siamese model" src="https://user-images.githubusercontent.com/48923446/108095927-68333300-70a6-11eb-91e0-0d80da4e0156.PNG">

# Loss Functions 
Siamese Network supports three types of loss functions, mainly:
  1) Contrastive Loss
  2) Triplet Loss 
  3) Quadruplet Loss
  
# Contrastive Loss
<img width="273" alt="contrastive l" src="https://user-images.githubusercontent.com/48923446/108096753-59994b80-70a7-11eb-81d7-b150611837dc.PNG">

<img width="307" alt="contrastiveeq" src="https://user-images.githubusercontent.com/48923446/108096761-5b630f00-70a7-11eb-8e0b-6c8921abeccf.PNG">

# Triplet Loss
![triplet loss d](https://user-images.githubusercontent.com/48923446/108096829-6fa70c00-70a7-11eb-8cfc-838c6d6a44c8.png)

<img width="325" alt="triplet loss" src="https://user-images.githubusercontent.com/48923446/108096841-72a1fc80-70a7-11eb-83b1-1ceeb36668b8.PNG">

# Quadruplet Loss
<img width="343" alt="quad" src="https://user-images.githubusercontent.com/48923446/108097210-db897480-70a7-11eb-8552-f682bf95c7fe.PNG">

# Data Loading
Intially when we downloaded the data from kaggle, the data was not in the right order to train a siamese network. 
We trained our model with triplet loss as a base metric. So we needed to send three inputs to the model at each iteration. These three inputs are called anchor, positive, negative images (as discussed in Triplet Loss section). To do this we reorgainzed the data manually.

<img width="437" alt="loading traindata" src="https://user-images.githubusercontent.com/48923446/108098168-1049fb80-70a9-11eb-8050-1000ca1a25f9.PNG">

# Preprocessing
The initial images were around (850,250,3) pixels. Using the same sized images for training the model would increase the computational complexity of the model. So we converted the images to binary images and then performed mathematical morphological operations. We resized the images to (250,75,1)

Code:

<img width="563" alt="image preprocessing" src="https://user-images.githubusercontent.com/48923446/108098581-8d757080-70a9-11eb-8635-dab1c7b260e5.PNG">

<img width="307" alt="before after" src="https://user-images.githubusercontent.com/48923446/108098827-db8a7400-70a9-11eb-93c3-b012b2936e81.PNG">
