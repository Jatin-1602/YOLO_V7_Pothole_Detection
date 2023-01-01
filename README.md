# YOLO_V7_Pothole_Detection

## Description

### [Dataverse Hack 2022](https://datahack.analyticsvidhya.com/contest/dataverse-hack/?utm_source=analyticsvidhya&utm_medium=datahack_navbar&utm_campaign=dataverse#About)

**Build a computer vision-based technology to process and detect the potholes present in an image** <br><br>

**Problem Statement** <br>
Over the past few years, the increase in the number of vehicles on road gave rise to the number of road accidents. According to a study, one fatal road accident occurs every 5 minutes in the country, and 8 die on roads every hour. This has become a major concern in the country. One of the primary causes of these road accidents is the management and maintenance of the roads. Potholes on roads can cause serious accidents, and any vehicle traveling at some decent speed can lose its track due to them. In the case of four-wheeler vehicles, potholes can cause severe damage to wheels and tires. More specifically, when it comes to two-wheelers like motorbikes, these vehicles are more prone to accidents due to potholes as the tendency to cause imbalance is very high and can lead to fatalities.

## Approach
Employed `YOLOv7` <br>
Given CSV file converted to YOLO format <br>
Used K-FOLD technique <br>

Training Hyperparameters:
* Environment : Google Colab
* Folds : 5
* Epochs : 33
* batch_size : 8
* img_size : 720 720
* weights : yolov7-e6e_training.pt

* hyperparameter : hyp.scratch.custom.yaml
* lr : 0.01
* conf : 0.05

## Result
Score : 0.456830354788351

## Evaluations
**FOLD_4** <br><br>

RESULT <br>
![results](https://user-images.githubusercontent.com/77826715/210163017-ba318255-6bf6-4ab0-af7e-d2564772ff09.png)

CONFUSION MATRIX <br>
![confusion_matrix](https://user-images.githubusercontent.com/77826715/210163067-9b5f21c5-f6f4-446b-a574-4bfba94efc22.png)

TRAIN_BATCH
![train_batch](https://user-images.githubusercontent.com/77826715/210163083-98473993-5e7f-41f8-b118-3609f80f20ab.jpg)


