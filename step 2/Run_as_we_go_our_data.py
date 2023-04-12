# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 22:42:56 2018

@author: Abdullah Nabil
"""
#import pandas as pd
#from google.colab import files
#import io
#uploaded = files.upload()
#dataframe_x = pd.read_csv(io.StringIO(uploaded['New_Form_data_Current_Quarter_1_trklts_x_y.txt'].decode('utf-8')))
#dataframe_y= pd.read_csv(io.StringIO(uploaded['New_Form_data_Next_Quarter_1_trklts_x_y.txt'].decode('utf-8')))
##
#for fn in uploaded.keys():
#  print('User uploaded file "{name}" with length {length} bytes'.format(name=fn, length=len(uploaded[fn])))
#  

#from array import array
import numpy
#import numpy as np
#import matplotlib.pyplot as plt
import pandas
#import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
#from sklearn.preprocessing import MinMaxScaler
#from sklearn.metrics import mean_squared_error

# fix random seed for reproducibility
numpy.random.seed(7)

#------------------
# load the dataset
#------------------
dataframe_x = pandas.read_csv('New_Form_data_Current_Quarter_1_trklts_x_y.txt', engine='python',header=None)
dataset_x = dataframe_x.values
dataframe_y = pandas.read_csv('New_Form_data_Next_Quarter_1_trklts_x_y.txt', engine='python',header=None)
dataset_y = dataframe_y.values
#-----------------------------
# normalize the dataset
min_x=1;
max_x=720;
min_y=1;
max_y=480;
dataset_x_n=dataset_x;
dataset_y_n=dataset_y;

dataset_x_n[:,0]=(dataset_x_n[:,0] - min_x) / ( max_x - min_x );
dataset_x_n[:,1]=(dataset_x[:,1] - min_y) / ( max_y - min_y );

dataset_x_n[:,2]=(dataset_x_n[:,2] - min_x) / ( max_x - min_x );
dataset_x_n[:,3]=(dataset_x[:,3] - min_y) / ( max_y - min_y );
           
dataset_x_n[:,4]=(dataset_x_n[:,4] - min_x) / ( max_x - min_x );
dataset_x_n[:,5]=(dataset_x[:,5] - min_y) / ( max_y - min_y );
#           
dataset_x_n[:,6]=(dataset_x_n[:,6] - min_x) / ( max_x - min_x );
dataset_x_n[:,7]=(dataset_x[:,7] - min_y) / ( max_y - min_y );
#           
#dataset_x_n[:,8]=(dataset_x_n[:,8] - min_x) / ( max_x - min_x );
#dataset_x_n[:,9]=(dataset_x[:,9] - min_y) / ( max_y - min_y );
#
#dataset_x_n[:,10]=(dataset_x_n[:,10] - min_x) / ( max_x - min_x );
#dataset_x_n[:,11]=(dataset_x[:,11] - min_y) / ( max_y - min_y );
#           
#dataset_x_n[:,12]=(dataset_x_n[:,12] - min_x) / ( max_x - min_x );
#dataset_x_n[:,13]=(dataset_x[:,13] - min_y) / ( max_y - min_y );
#           
#dataset_x_n[:,14]=(dataset_x_n[:,14] - min_x) / ( max_x - min_x );
#dataset_x_n[:,15]=(dataset_x[:,15] - min_y) / ( max_y - min_y );           
#           
#dataset_x_n[:,16]=(dataset_x_n[:,16] - min_x) / ( max_x - min_x );
#dataset_x_n[:,17]=(dataset_x[:,17] - min_y) / ( max_y - min_y );
#           
##dataset_x_n[:,0]=(dataset_x_n[:,0] - min_x) / ( max_x - min_x );
##dataset_x_n[:,1]=(dataset_x[:,1] - min_y) / ( max_y - min_y );
           
dataset_y_n[:,0]=(dataset_y_n[:,0] - min_x) / ( max_x - min_x );
dataset_y_n[:,1]=(dataset_y[:,1] - min_y) / ( max_y - min_y );

#-------------------------------
# split into train and test sets
#-------------------------------
#train_size = int(len(dataset_x) * 0.67)
train_size = int(len(dataset_x_n) * 1)
test_size = len(dataset_x_n) - train_size
train_x, test_x = dataset_x_n[0:train_size,:], dataset_x_n[train_size:len(dataset_x_n),:]
train_y, test_y = dataset_y_n[0:train_size,:], dataset_y_n[train_size:len(dataset_y_n),:]
print(len(train_x), len(test_x))
#---------------------------
# reshape into X=t and Y=t+1
#---------------------------
trainX = numpy.reshape(train_x, (train_x.shape[0], 1, train_x.shape[1]))
testX = numpy.reshape(test_x, (test_x.shape[0], 1, test_x.shape[1]))
#--------------------------------
# create and fit the LSTM network
#--------------------------------
model = Sequential()
model.add(LSTM(4, input_shape=(1,8)))
#model.add(Dense(1))
model.add(Dense(2))

#model.add(Dense(8))
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
#model.compile(loss='mean_squared_error', optimizer='adam')

model.fit(trainX, train_y, epochs=7, batch_size=1, verbose=1, validation_split=0.1)
#model.fit(trainX, train_y, epochs=10, batch_size=1, verbose=1)

#-----------------
# make predictions
#-----------------
trainPredict = model.predict(trainX)


#--------------------------------
# Saving the model
#--------------------------------
model.save_weights("Model_Quarter1.h5")
#: saves the weights of the model as a HDF5 file.
# model.get_weights(): returns a list of all weight tensors in the model, as Numpy arrays.
#numpy.savetxt("dataset_x_n_Quarter1.csv", dataset_x_n, delimiter=",")


#from google.colab import files
#files.download( "Model_Quarter1.h5" ) 





##------------------------------------------
## Testing Our Code by predicting One point.
##------------------------------------------
#
##Test_point=np.array([0.421000]);
#Test_point=np.array([[dataset_x_n[2,0], dataset_x_n[2,1],dataset_x_n[2,2], dataset_x_n[2,3],dataset_x_n[2,4], dataset_x_n[2,5],dataset_x_n[2,6], dataset_x_n[2,7]]]);
#r_e=numpy.reshape(Test_point, (Test_point.shape[0], 1, Test_point.shape[1]))
#ut=model.predict(r_e)
###Un Normlize the points again
#UNNormalized_Created_Point_x= min_x + ut[0,0]*(max_x - min_x);
#UNNormalized_Created_Point_y= min_y + ut[0,1]*(max_y - min_y);
### save the point to display it
#Created_Point=np.array([[UNNormalized_Created_Point_x,UNNormalized_Created_Point_y]])
###Created_Point = np.asarray(ut)
#numpy.savetxt("Created_Point.csv", Created_Point, delimiter=",")

##------------------------------------------
## Testing Our Code by predicting another point.
##------------------------------------------
#Test_point=np.array([[dataset_x_n[5,0], dataset_x_n[5,1],dataset_x_n[5,2], dataset_x_n[5,3],dataset_x_n[5,4], dataset_x_n[5,5],dataset_x_n[5,6], dataset_x_n[5,7]]]);
#r_e=numpy.reshape(Test_point, (Test_point.shape[0], 1, Test_point.shape[1]))
#ut=model.predict(r_e)
###Un Normlize the points again
#UNNormalized_Created_Point_x= min_x + ut[0,0]*(max_x - min_x);
#UNNormalized_Created_Point_y= min_y + ut[0,1]*(max_y - min_y);
### save the point to display it
#Created_Point_22=np.array([[UNNormalized_Created_Point_x,UNNormalized_Created_Point_y]])
###Created_Point = np.asarray(ut)
#numpy.savetxt("Created_Point_22.csv", Created_Point_22, delimiter=",")



##---------------------
##Forming One tracklet
##---------------------
#Test_point=np.array([[dataset_x_n[2,0], dataset_x_n[2,1],dataset_x_n[2,2], dataset_x_n[2,3],dataset_x_n[2,4], dataset_x_n[2,5],dataset_x_n[2,6], dataset_x_n[2,7]]]);
##       
#list_1=[]; 
#
#UNNormalized_Created_Point_x_1= min_x + Test_point[0,0]*(max_x - min_x);
#UNNormalized_Created_Point_y_1= min_y + Test_point[0,1]*(max_y - min_y);
#                                                   
#UNNormalized_Created_Point_x_2= min_x + Test_point[0,2]*(max_x - min_x);
#UNNormalized_Created_Point_y_2= min_y + Test_point[0,3]*(max_y - min_y);
#                                                   
#UNNormalized_Created_Point_x_3= min_x + Test_point[0,4]*(max_x - min_x);
#UNNormalized_Created_Point_y_3= min_y + Test_point[0,5]*(max_y - min_y);                                                   
#                                                   
#UNNormalized_Created_Point_x_4= min_x + Test_point[0,6]*(max_x - min_x);
#UNNormalized_Created_Point_y_4= min_y + Test_point[0,7]*(max_y - min_y);                                                  
#                                                   
#                                                   
#                                                   
##Test_point_Unnorm=np.array([[UNNormalized_Created_Point_x_2, UNNormalized_Created_Point_y_2]]);          
#list_1.append([UNNormalized_Created_Point_x_1, UNNormalized_Created_Point_y_1]);
#list_1.append([UNNormalized_Created_Point_x_2, UNNormalized_Created_Point_y_2]);
#list_1.append([UNNormalized_Created_Point_x_3, UNNormalized_Created_Point_y_3]);
#list_1.append([UNNormalized_Created_Point_x_4, UNNormalized_Created_Point_y_4]);
#
#temp_test_point=Test_point;                
## 
#for x in range(500):
##           
#    r_e=numpy.reshape(Test_point, (Test_point.shape[0], 1, Test_point.shape[1]))
#    ut=model.predict(r_e)
#    #list_1.append(ut[0,0], ut[0,1])
#    UNNormalized_Created_ut_x= min_x + ut[0,0]*(max_x - min_x);
#    UNNormalized_Created_ut_y= min_y + ut[0,1]*(max_y - min_y);
#    #ut_Unnorm=np.array([[UNNormalized_Created_ut_x_2, UNNormalized_Created_ut_y_2]]);          
#    list_1.append([UNNormalized_Created_ut_x,UNNormalized_Created_ut_y])
#    
#    Test_point=np.array([[temp_test_point[0,2], temp_test_point[0,3], temp_test_point[0,4], temp_test_point[0,5], temp_test_point[0,6], temp_test_point[0,7], ut[0,0], ut[0,1]]]);    
#    temp_test_point=Test_point
##       
#Created_Tracklet_Q4 = np.asarray(list_1)
#numpy.savetxt("Created_Tracklet_Q4.csv", Created_Tracklet_Q4, delimiter=",")
