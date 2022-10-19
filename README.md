# English Chatbot

## Introduction to the Project:    
    This is a simple chatbot Project in English. Using Java swing to develop GUI and python pytorch 
    to do the trainning and neural model.

    This Project only achieve seq2seq model and do not accomplish parallel training (Thus slow in training) 

    This Project is modified base on original Project : https://github.com/zhaoyingjun/chatbot (A Great Thanks!)

## Explain to Each Folder and File:
    ChatApp/: All Java GUI implemetation
    
    config/: all resource Path and some static parameter

    icons/: image resources

    train_data/: all train data and trained model

    data.py: formatting all the dialog inputs and creating dataset

    execute.py: do training

    runner.py: interface between Java GUI and pytorch model

    seq2seqModel.py: model class

## Recommend Environment:
    Java 8, Python: 3.8, Pytorch: 1.12
    other Package needed: Flask, numpy, nltk

## Running Procedures:
    There is already a 30-epoch training model base on the given dialog and wordlist
    So if just want to run without any more training, then type "python runner.py" in terminal

    If want to redo training by yourself, delete train_data/data_model.pt, and run "python execute.py"

    If want to redo training with your own data, delete train_data/data_model.pt, train_data/data_running.pt.
    And Strongly recommend go over the code data.py and execute.py to format your new dataset.


## 30 epoch trainning model example:


![alt text](./icons/chat_his.JPG?raw=true)