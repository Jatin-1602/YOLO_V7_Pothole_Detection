# Pothole_Detection_YOLO_V7

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
