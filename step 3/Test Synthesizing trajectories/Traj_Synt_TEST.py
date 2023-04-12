# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 22:42:56 2018

@author: Abdullah Nabil
"""
#from array import array
import numpy
import numpy as np
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

#----------------
#Load the models
#----------------
Model_Quarter1 = Sequential()
Model_Quarter1.add(LSTM(4, input_shape=(1,8)))
Model_Quarter1.add(Dense(2))
Model_Quarter1.compile(loss='mean_squared_error', optimizer='adam')
Model_Quarter1.load_weights("Model_Quarter1.h5")

Model_Quarter3 = Sequential()
Model_Quarter3.add(LSTM(4, input_shape=(1,8)))
Model_Quarter3.add(Dense(2))
Model_Quarter3.compile(loss='mean_squared_error', optimizer='adam')
Model_Quarter3.load_weights("Model_Quarter3.h5")

Model_Quarter4 = Sequential()
Model_Quarter4.add(LSTM(4, input_shape=(1,8)))
Model_Quarter4.add(Dense(2))
Model_Quarter4.compile(loss='mean_squared_error', optimizer='adam')
Model_Quarter4.load_weights("Model_Quarter4.h5")

Model_Quarter6 = Sequential()
Model_Quarter6.add(LSTM(4, input_shape=(1,8)))
Model_Quarter6.add(Dense(2))
Model_Quarter6.compile(loss='mean_squared_error', optimizer='adam')
Model_Quarter6.load_weights("Model_Quarter6.h5")

Model_Quarter7 = Sequential()
Model_Quarter7.add(LSTM(4, input_shape=(1,8)))
Model_Quarter7.add(Dense(2))
Model_Quarter7.compile(loss='mean_squared_error', optimizer='adam')
Model_Quarter7.load_weights("Model_Quarter7.h5")

Model_Quarter8 = Sequential()
Model_Quarter8.add(LSTM(4, input_shape=(1,8)))
Model_Quarter8.add(Dense(2))
Model_Quarter8.compile(loss='mean_squared_error', optimizer='adam')
Model_Quarter8.load_weights("Model_Quarter8.h5")

Model_Quarter9 = Sequential()
Model_Quarter9.add(LSTM(4, input_shape=(1,8)))
Model_Quarter9.add(Dense(2))
Model_Quarter9.compile(loss='mean_squared_error', optimizer='adam')
Model_Quarter9.load_weights("Model_Quarter9.h5")
#Model_Quarter3 = Sequential()
#Model_Quarter3.add(LSTM(4, input_shape=(1,4)))
#Model_Quarter3.add(Dense(2))
#Model_Quarter3.compile(loss='mean_squared_error', optimizer='adam')
#Model_Quarter3.load_weights("Model_Quarter3.h5")
#
#Model_Quarter4 = Sequential()
#Model_Quarter4.add(LSTM(4, input_shape=(1,4)))
#Model_Quarter4.add(Dense(2))
#Model_Quarter4.compile(loss='mean_squared_error', optimizer='adam')
#Model_Quarter4.load_weights("Model_Quarter4.h5")
#------------------
# load the test Tracks
#------------------
Tracks_UN = pandas.read_csv('Entrance_tracks.csv', engine='python')
Tracks_UN_values = Tracks_UN.values
#-----------------------------
# Load the motion Map
#-----------------------------
Motion_Map = pandas.read_csv('map_dilated3.csv', engine='python')
Motion_Map = Motion_Map.values
#-----------------------------
# normalize the tracks
min_x=1;
max_x=720;
min_y=1;
max_y=480;
Tracks_N_values=Tracks_UN_values;
#Tracks_UN_values_before_norm=Tracks_UN_values;
#Tracks_N_values[:,1]=(Tracks_UN_values[:,1] - min_x) / ( max_x - min_x );
#Tracks_N_values[:,2]=(Tracks_UN_values[:,2] - min_y) / ( max_y - min_y );
#
#Tracks_N_values[:,3]=(Tracks_UN_values[:,3] - min_x) / ( max_x - min_x );
#Tracks_N_values[:,4]=(Tracks_UN_values[:,4] - min_y) / ( max_y - min_y );
#           
#Tracks_N_values[:,5]=(Tracks_UN_values[:,5] - min_x) / ( max_x - min_x );
#Tracks_N_values[:,6]=(Tracks_UN_values[:,6] - min_y) / ( max_y - min_y );
#           
#Tracks_N_values[:,7]=(Tracks_UN_values[:,7] - min_x) / ( max_x - min_x );
#Tracks_N_values[:,8]=(Tracks_UN_values[:,8] - min_y) / ( max_y - min_y );
#
Tracks_N_values[:,1]=(Tracks_UN_values[:,1] - min_x) / ( max_x - min_x );
Tracks_N_values[:,2]=(Tracks_UN_values[:,2] - min_y) / ( max_y - min_y );

Tracks_N_values[:,3]=(Tracks_UN_values[:,3] - min_x) / ( max_x - min_x );
Tracks_N_values[:,4]=(Tracks_UN_values[:,4] - min_y) / ( max_y - min_y );
           
Tracks_N_values[:,5]=(Tracks_UN_values[:,5] - min_x) / ( max_x - min_x );
Tracks_N_values[:,6]=(Tracks_UN_values[:,6] - min_y) / ( max_y - min_y );
#           
Tracks_N_values[:,7]=(Tracks_UN_values[:,7] - min_x) / ( max_x - min_x );
Tracks_N_values[:,8]=(Tracks_UN_values[:,8] - min_y) / ( max_y - min_y );
#
#Tracks_N_values[:,9]=(Tracks_UN_values[:,9] - min_x) / ( max_x - min_x );
#Tracks_N_values[:,10]=(Tracks_UN_values[:,10] - min_y) / ( max_y - min_y );
#
#Tracks_N_values[:,11]=(Tracks_UN_values[:,11] - min_x) / ( max_x - min_x );
#Tracks_N_values[:,12]=(Tracks_UN_values[:,12] - min_y) / ( max_y - min_y );
#           
#Tracks_N_values[:,13]=(Tracks_UN_values[:,13] - min_x) / ( max_x - min_x );
#Tracks_N_values[:,14]=(Tracks_UN_values[:,14] - min_y) / ( max_y - min_y );
#           
#Tracks_N_values[:,15]=(Tracks_UN_values[:,15] - min_x) / ( max_x - min_x );
#Tracks_N_values[:,16]=(Tracks_UN_values[:,16] - min_y) / ( max_y - min_y );
#               
#Tracks_N_values[:,17]=(Tracks_UN_values[:,17] - min_x) / ( max_x - min_x );
#Tracks_N_values[:,18]=(Tracks_UN_values[:,18] - min_y) / ( max_y - min_y );               
#******************************************************************************
#                       Start Trajectory Generation
#******************************************************************************

No_Trajectories=len(Tracks_N_values);
list_all=[];
#for x in range(0, No_Trajectories-1):
for x in range(700,800):
    x
    list_1=[];
    #Test_point=np.array([[Tracks_N_values[1,1], Tracks_N_values[1,2],Tracks_N_values[1,3], Tracks_N_values[1,4],Tracks_N_values[1,5], Tracks_N_values[1,6],Tracks_N_values[1,7],Tracks_N_values[1,8]]]);
    Test_point=np.array([[Tracks_N_values[x,1], Tracks_N_values[x,2],Tracks_N_values[x,3], Tracks_N_values[x,4], Tracks_N_values[x,5], Tracks_N_values[x,6], Tracks_N_values[x,7], Tracks_N_values[x,8]]]);
    UNNormalized_Created_Point_x_1= min_x + Test_point[0,0]*(max_x - min_x);
    UNNormalized_Created_Point_y_1= min_y + Test_point[0,1]*(max_y - min_y);
    UNNormalized_Created_Point_x_2= min_x + Test_point[0,2]*(max_x - min_x);
    UNNormalized_Created_Point_y_2= min_y + Test_point[0,3]*(max_y - min_y);
    UNNormalized_Created_Point_x_3= min_x + Test_point[0,4]*(max_x - min_x);
    UNNormalized_Created_Point_y_3= min_y + Test_point[0,5]*(max_y - min_y);                                                   
    UNNormalized_Created_Point_x_4= min_x + Test_point[0,6]*(max_x - min_x);
    UNNormalized_Created_Point_y_4= min_y + Test_point[0,7]*(max_y - min_y);
#    UNNormalized_Created_Point_x_5= min_x + Test_point[0,8]*(max_x - min_x);
#    UNNormalized_Created_Point_y_5= min_y + Test_point[0,9]*(max_y - min_y);
#    UNNormalized_Created_Point_x_6= min_x + Test_point[0,10]*(max_x - min_x);
#    UNNormalized_Created_Point_y_6= min_y + Test_point[0,11]*(max_y - min_y);
#    UNNormalized_Created_Point_x_7= min_x + Test_point[0,12]*(max_x - min_x);
#    UNNormalized_Created_Point_y_7= min_y + Test_point[0,13]*(max_y - min_y);                                                   
#    UNNormalized_Created_Point_x_8= min_x + Test_point[0,14]*(max_x - min_x);
#    UNNormalized_Created_Point_y_8= min_y + Test_point[0,15]*(max_y - min_y); 
#    UNNormalized_Created_Point_x_9= min_x + Test_point[0,16]*(max_x - min_x);
#    UNNormalized_Created_Point_y_9= min_y + Test_point[0,17]*(max_y - min_y);
    list_1.append([UNNormalized_Created_Point_x_1, UNNormalized_Created_Point_y_1]);
    list_1.append([UNNormalized_Created_Point_x_2, UNNormalized_Created_Point_y_2]);
    list_1.append([UNNormalized_Created_Point_x_3, UNNormalized_Created_Point_y_3]);
    list_1.append([UNNormalized_Created_Point_x_4, UNNormalized_Created_Point_y_4]);
#    list_1.append([UNNormalized_Created_Point_x_5, UNNormalized_Created_Point_y_5]);
#    list_1.append([UNNormalized_Created_Point_x_6, UNNormalized_Created_Point_y_6]);
#    list_1.append([UNNormalized_Created_Point_x_7, UNNormalized_Created_Point_y_7]);
#    list_1.append([UNNormalized_Created_Point_x_8, UNNormalized_Created_Point_y_8]);
#    list_1.append([UNNormalized_Created_Point_x_9, UNNormalized_Created_Point_y_9]);             

#    #--------------------------------------------------------------------------
#    #Find the model that have the last point
    if ( UNNormalized_Created_Point_x_4 > 0 and UNNormalized_Created_Point_x_4 <= 240 and UNNormalized_Created_Point_y_4 > 0 and UNNormalized_Created_Point_y_4 <= 160):
       Model=Model_Quarter1
    elif (UNNormalized_Created_Point_x_4>480 and UNNormalized_Created_Point_x_4<=720 and UNNormalized_Created_Point_y_4>0 and UNNormalized_Created_Point_y_4<=160):
       Model=Model_Quarter3
    elif (UNNormalized_Created_Point_x_4>0 and UNNormalized_Created_Point_x_4<=240 and UNNormalized_Created_Point_y_4>160 and UNNormalized_Created_Point_y_4<=320):
       Model=Model_Quarter4
    elif (UNNormalized_Created_Point_x_4>480 and UNNormalized_Created_Point_x_4<=720 and UNNormalized_Created_Point_y_4>160 and UNNormalized_Created_Point_y_4<=320):
       Model=Model_Quarter6
    elif (UNNormalized_Created_Point_x_4>0 and UNNormalized_Created_Point_x_4<=240 and UNNormalized_Created_Point_y_4>320 and UNNormalized_Created_Point_y_4<=480):
       Model=Model_Quarter7
    elif (UNNormalized_Created_Point_x_4>240 and UNNormalized_Created_Point_x_4<=480 and UNNormalized_Created_Point_y_4>320 and UNNormalized_Created_Point_y_4<=480):
       Model=Model_Quarter8
    elif (UNNormalized_Created_Point_x_4>480 and UNNormalized_Created_Point_x_4<=720 and UNNormalized_Created_Point_y_4>320 and UNNormalized_Created_Point_y_4<=480):
       Model=Model_Quarter9
    #Model=Model_Quarter2

    #**************************************************************************   
    #Start the Prediction process.   
    #**************************************************************************
    Flag=1;
    while Flag != 0:
        #--------------------------------------------------------------------------
        # Predicting the next point using the selected Model
        r_e=numpy.reshape(Test_point, (Test_point.shape[0], 1, Test_point.shape[1]));
        ut=Model.predict(r_e);
        UNNormalized_Created_ut_x= min_x + ut[0,0]*(max_x - min_x);
        UNNormalized_Created_ut_y= min_y + ut[0,1]*(max_y - min_y);
#         #Find the model that have the last point
        if ( UNNormalized_Created_ut_x > 0 and UNNormalized_Created_ut_x <= 240 and UNNormalized_Created_ut_y > 0 and UNNormalized_Created_ut_y <= 160):
            Model=Model_Quarter3
        elif (UNNormalized_Created_ut_x>480 and UNNormalized_Created_ut_x<=720 and UNNormalized_Created_ut_y>0 and UNNormalized_Created_ut_y<=160):
            Model=Model_Quarter3
        elif (UNNormalized_Created_ut_x>0 and UNNormalized_Created_ut_x<=240 and UNNormalized_Created_ut_y>160 and UNNormalized_Created_ut_y<=320):
            Model=Model_Quarter4
        elif (UNNormalized_Created_ut_x>480 and UNNormalized_Created_ut_x<=720 and UNNormalized_Created_ut_y>160 and UNNormalized_Created_ut_y<=320):
            Model=Model_Quarter6  
        elif ( UNNormalized_Created_ut_x > 0 and UNNormalized_Created_ut_x <= 240 and UNNormalized_Created_ut_y>320 and UNNormalized_Created_ut_y<=480):
            Model=Model_Quarter7
        elif (UNNormalized_Created_ut_x>240 and UNNormalized_Created_ut_x<=480 and UNNormalized_Created_ut_y>320 and UNNormalized_Created_ut_y<=480):
            Model=Model_Quarter8
        elif (UNNormalized_Created_ut_x>480 and UNNormalized_Created_ut_x<=720 and UNNormalized_Created_ut_y>320 and UNNormalized_Created_ut_y<=480):
           Model=Model_Quarter9


        if UNNormalized_Created_ut_y >= 480 or UNNormalized_Created_ut_x >= 720:
            break
        #--------------------------------------------------------------------------
        # Test if the point is inside the motion map to add it to list and predict 
        Flag=Motion_Map[int(UNNormalized_Created_ut_y)-1,int(UNNormalized_Created_ut_x)-1];
        #Flag=1;
        if Flag==1:
           list_1.append([UNNormalized_Created_ut_x,UNNormalized_Created_ut_y]);
           temp_test_point=Test_point;
           Test_point=np.array([[temp_test_point[0,2], temp_test_point[0,3], temp_test_point[0,4], temp_test_point[0,5], temp_test_point[0,6], temp_test_point[0,7], ut[0,0], ut[0,1]]]);    
        else:
            #Quit the current iteration (Trajectory) and start a new iteration (Trajectory).
           break
        if len(list_1)>2500:
              break
    list_all.append(list_1);
Created_Traj_M1 = np.asarray(list_all[0])
numpy.savetxt("Created_Traj_M1.csv", Created_Traj_M1, delimiter=",")

Created_Traj_M2 = np.asarray(list_all[25])
numpy.savetxt("Created_Traj_M2.csv", Created_Traj_M2, delimiter=",")

Created_Traj_M3 = np.asarray(list_all[50])
numpy.savetxt("Created_Traj_M3.csv", Created_Traj_M3, delimiter=",")

Created_Traj_M4 = np.asarray(list_all[75])
numpy.savetxt("Created_Traj_M4.csv", Created_Traj_M4, delimiter=",")

Created_Traj_M5 = np.asarray(list_all[60])
numpy.savetxt("Created_Traj_M5.csv", Created_Traj_M5, delimiter=",")


#Created_Traj_M1 = np.asarray(list_all[7])
#numpy.savetxt("Created_Traj_M1.csv", Created_Traj_M1, delimiter=",")
#
#Created_Traj_M2 = np.asarray(list_all[25])
#numpy.savetxt("Created_Traj_M2.csv", Created_Traj_M2, delimiter=",")
#
#Created_Traj_M3 = np.asarray(list_all[77])
#numpy.savetxt("Created_Traj_M3.csv", Created_Traj_M3, delimiter=",")
#
#Created_Traj_M4 = np.asarray(list_all[92])
#numpy.savetxt("Created_Traj_M4.csv", Created_Traj_M4, delimiter=",")
#
#Created_Traj_M5 = np.asarray(list_all[98])
#numpy.savetxt("Created_Traj_M5.csv", Created_Traj_M5, delimiter=",")