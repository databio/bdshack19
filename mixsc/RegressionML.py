#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thurs Mar 7 2019
Updated on Fri Mar 8 2019 to include MLP model

Predicting Changes in LVESV Post-CRT with Regression Models

Regression Models Included in Analysis:
    1. Linear Regression (LR)
    2. Random Forest Regression (RF)
    3. Support Vector Machine Regression (SVM)
    4. Multi-Layer Perceptron Regression (MLP)

This script trains each model with the same training data while also testing
each model with the same testing data (through cross-validation)

Hyperparameters for RF, SVM, and MLP were optimized using 'GridSearchCV'

@author: derekbivona
"""

# -----------------------------------------------------------------------------
# NOTE: To load .mat file:
# import scipy.io as sio
# mat = sio.loadmat('rfdata.mat')
# -----------------------------------------------------------------------------

# Import necessary modules
import numpy  as np
import pandas as pd
import scipy  as sp

# Import sci kit learn
import sklearn
from sklearn import linear_model
from sklearn import ensemble
from sklearn import svm
from sklearn import neural_network
from sklearn import model_selection
from sklearn import linear_model
from sklearn import metrics
from sklearn.model_selection import GridSearchCV

#%% Pre-Allocate Appropriate Arrays for Optimized Regression Models
    
# Pre-allocate regressor accuracy (r-squared) array that will be calculated 
# with the 'score' attribute from the model
accLR  = []
accRF  = []
accSVM = [] 
accMLP = []  

# Pre-allocate arrays to save training and testing data for every split with 
# every subset of important features (with optimized hyperparameters - outer
# loop of cross-validation)
XtrainALL = []
YtrainALL = []    
XtestALL  = []
YtestALL  = []

# Pre-allocate array to save model predictions for every split with every 
# subset of important features
YpredLR  = []
YpredRF  = []
YpredSVM = []
YpredMLP = []

# Pre-allocate mean absolute error, mean squared error, and
# root mean squared error for linear regression
MeanAbsErrLR   = []
MeanSqErrLR    = []
RtMeanSqErrLR  = []
RsquaredLR     = []

# Pre-allocate mean absolute error, mean squared error, and
# root mean squared error for random forest regression
MeanAbsErrRF   = []
MeanSqErrRF    = []
RtMeanSqErrRF  = []
RsquaredRF     = []

# Pre-allocate mean absolute error, mean squared error, and
# root mean squared error for support vector machine regression
MeanAbsErrSVM   = []
MeanSqErrSVM    = []
RtMeanSqErrSVM  = []
RsquaredSVM     = []

# Pre-allocate mean absolute error, mean squared error, and
# root mean squared error for multi-layer perceptron regression
MeanAbsErrMLP   = []
MeanSqErrMLP    = []
RtMeanSqErrMLP  = []
RsquaredMLP     = []

# Pre-allocate array to store average r-squared and root-mean-squared-error 
# scores for every subset of features (with optimized model)
# Linear Regression
RsqLR  = []
RMSELR = []

# Pre-allocate array to store average r-squared and root-mean-squared-error 
# scores for every subset of features (with optimized model)
# Random Forest
RsqRF  = []
RMSERF = []

# Pre-allocate array to store average r-squared and root-mean-squared-error 
# scores for every subset of features (with optimized model)
# Support Vector Machine
RsqSVM  = []
RMSESVM = []

# Pre-allocate array to store average r-squared and root-mean-squared-error 
# scores for every subset of features (with optimized model)
# Multi-Layer Perceptron
RsqMLP  = []
RMSEMLP = []

#%% Read in Original Data    
df_crt = pd.read_csv('CRT_MI.csv',header=0)

# Under gender, replace 'Male' as 1 and 'Female' as 0
df_crt = df_crt.replace(['Male','Female'],[1, 0])

# Convert data frame to array
data = np.array(df_crt)

# Separate data into features & target variable
# Target variable should be last column in csv file

# Define features
X = data[:,0:np.shape(data)[1]-1]

# Standardize continuous features
# Define indices of continuous variables
cont = [1, 2, 3, 4, 5, 6, 8]

# Calculate mean and standard deviation of each continous feature
meanX = np.mean(X[:,cont],axis=0)
stdX  = np.std(X[:,cont],axis=0)

# Place standardized (continuous) features into the feature matrix
X[:,cont] = (X[:,cont] - meanX)/stdX

X = X[:,cont]

# Define target variable
Y = data[:,np.shape(data)[1]-1]

#%% Run Regression Models

# Set number of folds
k1 = 10 # fold-number used to test performance of optimized models

# Set hyperparameter range to be used in 'GridSearchCV':

# paramRF  = {'n_estimators':[20, 15, 20, 25, 30]}

paramRF  = {'n_estimators':[int(x) for x in np.linspace(start = 10, stop = 100, num = 10)],
                            'max_features':['auto','sqrt'],
                            'bootstrap':['True','False']}

paramSVM = {'kernel':('linear','rbf'),
                 'C':[0.001, 0.1, 1, 10, 100],
                 'gamma':[0.001, 0.01, 0.1, 1]}

paramMLP = {
    'hidden_layer_sizes': [(50,50,50), (50,100,50), (100,)],
    'activation': ['tanh', 'relu'],
    'solver': ['sgd', 'adam'],
    'alpha': [0.0001, 0.05],
    'learning_rate': ['constant','adaptive'],
}

# Perfrom cross validation with n_splits = number of folds (k1)
kf = sklearn.model_selection.KFold(n_splits=k1,shuffle=True)

# Loop through the training and testing splits
tk = 0
for train_index, test_index in kf.split(X):

    # Split data into training & testing sets
    X_train, X_test = np.array(X[train_index]), np.array(X[test_index])
    Y_train, Y_test = np.array(Y[train_index]), np.array(Y[test_index])

    # Save training data
    XtrainALL.append(X_train)
    YtrainALL.append(Y_train)

    # Save testing data
    XtestALL.append(X_test)
    YtestALL.append(Y_test)

    # Train and test linear regression model
    accLR.append(sklearn.linear_model.
    LinearRegression().fit(X_train,Y_train).score(X_test, Y_test))    
    y_pred_LR  = sklearn.linear_model.LinearRegression().fit(X_train, Y_train).predict(X_test)
    YpredLR.append(y_pred_LR)
    
    # Train and test random forest regression model
    RF     = ensemble.RandomForestRegressor(criterion='mse')
    clf_rf = GridSearchCV(RF, paramRF, cv=5)
    accRF.append(clf_rf.fit(X_train, Y_train).best_estimator_.score(X_test,Y_test))
    y_pred_RF  = clf_rf.fit(X_train, Y_train).best_estimator_.predict(X_test)
    YpredRF.append(y_pred_RF)      
    
    # Train and test support vector machine regression model
    SVM    = svm.SVR()
    clf_svm = GridSearchCV(SVM, paramSVM, cv=5)
    accSVM.append(clf_svm.fit(X_train, Y_train).best_estimator_.score(X_test,Y_test))   
    y_pred_SVM  = clf_svm.fit(X_train, Y_train).best_estimator_.predict(X_test)
    YpredSVM.append(y_pred_SVM)
    
    # Train and test multi-layer perceptron regression model
    MLP = sklearn.neural_network.MLPRegressor(max_iter=500)
    clf_mlp = GridSearchCV(MLP, paramMLP, n_jobs=-1, cv=5)
    accMLP.append(clf_mlp.fit(X_train,Y_train).best_estimator_.score(X_test, Y_test))    
    y_pred_MLP  = clf_mlp.fit(X_train,Y_train).best_estimator_.fit(X_test, Y_test).predict(X_test)
    YpredMLP.append(y_pred_MLP)
    
    # Store model performance metrics for linear regression
    MeanAbsErrLR.append(metrics.mean_absolute_error(Y_test,y_pred_LR))
    MeanSqErrLR.append(metrics.mean_squared_error(Y_test,y_pred_LR))
    RtMeanSqErrLR.append(np.sqrt(metrics.mean_squared_error(Y_test,y_pred_LR)))
    RsquaredLR.append(metrics.r2_score(Y_test,y_pred_LR))
    
    # Store model performance metrics for random forest regression
    MeanAbsErrRF.append(metrics.mean_absolute_error(Y_test,y_pred_RF))
    MeanSqErrRF.append(metrics.mean_squared_error(Y_test,y_pred_RF))
    RtMeanSqErrRF.append(np.sqrt(metrics.mean_squared_error(Y_test,y_pred_RF)))
    RsquaredRF.append(metrics.r2_score(Y_test,y_pred_RF))
    
    # Store model performance metrics for support vector machine regression
    MeanAbsErrSVM.append(metrics.mean_absolute_error(Y_test,y_pred_SVM))
    MeanSqErrSVM.append(metrics.mean_squared_error(Y_test,y_pred_SVM))
    RtMeanSqErrSVM.append(np.sqrt(metrics.mean_squared_error(Y_test,y_pred_SVM)))
    RsquaredSVM.append(metrics.r2_score(Y_test,y_pred_SVM))
    
    # Store model performance metrics for multi-layer perceptron regression
    MeanAbsErrMLP.append(metrics.mean_absolute_error(Y_test,y_pred_MLP))
    MeanSqErrMLP.append(metrics.mean_squared_error(Y_test,y_pred_MLP))
    RtMeanSqErrMLP.append(np.sqrt(metrics.mean_squared_error(Y_test,y_pred_MLP)))
    RsquaredMLP.append(metrics.r2_score(Y_test,y_pred_MLP))
    
    tk += 1
        
    print 'Completed fold %d!' % (tk)    

    
#%% Calculate Model Performance per Subset of Features

# Calculate the average r-squared over the 10 training/testing sets per 
# subset of important features
RsqLR.append((np.sum(RsquaredLR))/k1)
RsqRF.append((np.sum(RsquaredRF))/k1)
RsqSVM.append((np.sum(RsquaredSVM))/k1)
RsqMLP.append((np.sum(RsquaredMLP))/k1)

# Calculate the average RMSE over the 10 training/testing sets per 
# subset of important features
RMSELR.append((np.sum(RtMeanSqErrLR))/k1)
RMSERF.append((np.sum(RtMeanSqErrRF))/k1)
RMSESVM.append((np.sum(RtMeanSqErrSVM))/k1)
RMSEMLP.append((np.sum(RtMeanSqErrMLP))/k1)

#%% Plot R-squared values

# Prepare data for plot
LRdata  = np.transpose(RsquaredLR)
RFdata  = np.transpose(RsquaredRF)
SVMdata = np.transpose(RsquaredSVM)
MLPdata = np.transpose(RsquaredMLP)

# Import 'matplotlib'
import matplotlib.pyplot as plt

# Import seaborn which is a python data visualization library 
# based on 'matplotlib'
import seaborn as sns

plt.figure(1)

sns.set_style("white")
sns.despine()

# Plot swarm plot
ax = sns.swarmplot(data=[LRdata, RFdata, SVMdata, MLPdata], 
                   size=10)

# Plot box plots
# ax = sns.boxplot(data=[accuracy_DT, accuracy_RF, accuracy_AB, accuracy_SVM,
                       # accuracy_KNN],boxprops={'facecolor':'None'})
                       
ax.set(ylim=(0,1.05))
fig = ax.get_figure()
#fig.savefig('PreCRTParameters_SwarmPlot_10fold_FeatSelect.png', dpi=1200)