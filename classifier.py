import cv2
import glob
import random
import numpy as np
import os
import pickle
import numpy as np
from matplotlib import pyplot as plt
import subprocess
#from Tkinter import *
from PIL import ImageTk,Image
import Tkinter as tk
emotions = ["neutral", "anger", "contempt", "disgust", "fear", "happy", "sadness", "surprise"] #Emotion list
fishface = cv2.createFisherFaceRecognizer() #Initialize fisher face classifier

data = {}

def get_training_data(emotion): #Define function to get file list, randomly shuffle it and split 80/20
    files = glob.glob("dataset\\%s\\*" %emotion)
    random.shuffle(files)
    training = files[:int(len(files)*0.5)] #get first 80% of file list
    return training

def get_prediction_data():
    file=glob.glob("test_images\\*")
    prediction=file
    #print(prediction)
    return prediction

def make_sets():
    training_data = []
    training_labels = []
    prediction_data = []
    prediction_labels = []
    for emotion in emotions:
        training = get_training_data(emotion)
        #Append data to training and prediction list, and generate labels 0-7
        for item in training:
            image = cv2.imread(item) #open image
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #convert to grayscale
            training_data.append(gray) #append image array to training data list
            training_labels.append(emotions.index(emotion))
    
    prediction=get_prediction_data()
    for item in prediction: #repeat above process for prediction set
            image = cv2.imread(item)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            prediction_data.append(gray)
            prediction_labels.append(emotions.index(emotion))    

    return training_data, training_labels, prediction_data, prediction_labels

def run_recognizer():
    training_data, training_labels, prediction_data, prediction_labels = make_sets()
    
    print "training fisher face classifier"
    print "size of training set is:", len(training_labels), "images"
    #fishface.train(training_data, np.asarray(training_labels))
    #fishface.save("test.yml")
    fishface.load("test.yml")
  
    print "predicting classification set"
    
    count_array=np.array([0,0,0,0,0,0,0,0])

    for image in prediction_data:
        pred, conf = fishface.predict(image)
        count_array[pred]+=1
        #pack [ttk::progressbar .p2 -orient horizontal -length 200 -mode determinate -variable a-maximum 75 -value num]
        #print(emotions[pred])

    #print(count_array)
    #print(count_array.argmax())
    #print(count_array.sum())
    total=count_array.sum()
    #print(total)
    for i in range(0,8):
        count_array[i]=count_array[i]*(100/total)
    #print(count_array)    
    return count_array

result = run_recognizer()
max_emotion=result.argmax()
print "Displaying Emotions Percentages"
for i in range(0,8):
    #print emotions[i]," :",result[i],"%"
    print "%8s : %s" % (emotions[i],result[i]),"%"
print "Overall emotion is" ,emotions[max_emotion]
def  plot():
    OX=emotions
    OY=result
    fig = plt.figure()
    width = .35
    ind = np.arange(len(OY))
    plt.bar(ind, OY, width=width)
    plt.xticks(ind + width / 2, OX)
    fig.autofmt_xdate()
    plt.savefig("figure.pdf")
plot()
#os.system("figure.pdf")
subprocess.Popen("figure.pdf",shell=True)
def smiley():
    # app = tk.Tk()
    # string="emotions\\"+emotions[max_emotion]+".jpg"
    # temp=Image.open(string)
    # temp = temp.save("photo.ppm","ppm")
    # photo = ImageTK.PhotoImage(file = "photo.ppm")
    # imagepanel=Label(app,image = photo)
    # imagepanel.grid()
    # app.mainloop()
    

    #path = 'C:/xxxx/xxxx.jpg'
    #root = tk.Tk()
    # img = ImageTk.PhotoImage(Image.open(string))
    # panel = tk.Label(app, image = img)
    # panel.pack(side = "bottom", fill = "both", expand = "yes")
    # app.mainloop()

    root = tk.Tk()  
    string="emotions\\"+emotions[max_emotion]+".jpg"
    image = Image.open(string)
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(root, image=photo)
    label.image = photo
    label.grid(row=2, column=0)
    #Start the program
    root.mainloop()



#smiley()

