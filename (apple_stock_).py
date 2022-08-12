# -*- coding: utf-8 -*-
"""(Apple stock )Deep Learning Project Submission Date (08 May, 2022): Evaluation of Tree Based Ensemble Machine Learning Models in Predicting Stock Price Direction of Movement.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OaUgBzTb9z3FoWXltcjdUtSdpf6xeFp6
"""

#importing libraries
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
!pip install yfinance
import yfinance as yf
from pandas_datareader import data as pdr
import datetime as date
#!pip install ta-lib
from sklearn.metrics import accuracy_score

from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score, roc_curve, auc
from sklearn.metrics import confusion_matrix

#reading the data
apple = pd.read_csv('/content/drive/MyDrive/STOCK EXCHANGE DATASETS AND CODINGS/Technology Stock Forecasting Complete/Stock Exchange Research task/AAPL.csv')
apple

#Technical Indicators
ema_26 = apple['Close'].transform(lambda x:x.ewm(span=26).mean())
ema_26

ema_12 = apple['Close'].transform(lambda x:x.ewm(span=12).mean())
ema_12

# Commented out IPython magic to ensure Python compatibility.
!wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
!tar -xzvf ta-lib-0.4.0-src.tar.gz
# %cd ta-lib
!./configure --prefix=/usr
!make
!make install
!pip install Ta-Lib
import talib as ta

ema_12 = apple['Close'].transform(lambda x:x.ewm(span=12).mean())
macdd=ema_12-ema_26
ema_9_macd=macdd.ewm(span=9).mean()
n=14
low_14=apple['Low'].transform(lambda x:x.rolling(window=n).min())
high_14=apple['High'].transform(lambda x:x.rolling(window=n).max())
k_percent=100*((apple['Close']-low_14)/(high_14-low_14))

#Relative Strength Index (RSI)
apple['RSI'] = ta.RSI(apple['Close'], timeperiod=14)

#MACD, short for moving average convergence/divergence, is a trading indicator used in technical analysis of stock prices

apple['macd'], apple['macdsignal'], apple['macdhist'] = ta.MACD(apple['Close'], fastperiod=12, slowperiod=26, signalperiod=9)

# The Willspread is more of a market strength indicator, it displays which of two markets is stronger, and can help determine if a symbol is strong or....
# ... weak compared to the overall market, depending on the secondary input. Hence the comparison to bonds when trading stocks or indexes, or to gold if trading bonds.

apple['WILL'] = ta.WILLR(apple['High'], apple['Low'], apple['Close'], timeperiod=14)
apple['MACD']=macdd
apple['MACD_EMA']=ema_9_macd
apple['STOCHOSI']=k_percent

apple['ADXR'] = ta.ADXR(apple['High'], apple['Low'], apple['Close'], timeperiod=10)
apple['APO'] = ta.APO(apple['Close'], fastperiod=12, slowperiod=26, matype=0)
apple['aroondown'], apple['aroonup'] = ta.AROON(apple['High'], apple['Low'], timeperiod=14)
apple['AROONOSC'] = ta.AROONOSC(apple['High'], apple['Low'], timeperiod=14)
apple['BOP'] = ta.BOP(apple['Open'], apple['High'], apple['Low'], apple['Close'])
apple['CCI'] = ta.CCI(apple['High'], apple['Low'], apple['Close'], timeperiod=14)
apple['CMO']= ta.CMO(apple['Close'], timeperiod=14)
apple['DX']= ta.DX(apple['High'], apple['Low'], apple['Close'], timeperiod=14)
apple['macdext'], apple['macdextsignal'], apple['macdexthist'] = ta.MACDEXT(apple['Close'], fastperiod=12, fastmatype=0, slowperiod=26, slowmatype=0, signalperiod=9, signalmatype=0)
apple['macdfix'], apple['macdfixsignal'], apple['macdfixhist'] = ta.MACDFIX(apple['Close'], signalperiod=9)

apple['MINUS_DI'] = ta.MINUS_DI(apple['High'], apple['Low'], apple['Close'], timeperiod=14)
apple['MINUS_DM'] = ta.MINUS_DM(apple['High'], apple['Low'], timeperiod=14)
apple['MOM'] = ta.MOM(apple['Close'], timeperiod=10)
apple['PLUS_DI'] = ta.PLUS_DI(apple['High'], apple['Low'], apple['Close'], timeperiod=14)
apple['PLUS_DM'] = ta.PLUS_DM(apple['High'], apple['Low'], timeperiod=14)
apple['PPO'] = ta.PPO(apple['Close'], fastperiod=12, slowperiod=26, matype=0)
apple['ROC']= ta.ROC(apple['Close'], timeperiod=10)
apple['ROCP'] = ta.ROCP(apple['Close'], timeperiod=10)
apple['ROCR'] = ta.ROCR(apple['Close'], timeperiod=10)
apple['STOCHk'], apple['STOCHd'] = ta.STOCH(apple['High'], apple['Low'], apple['Close'], fastk_period=5, slowk_period=3,slowk_matype=0, slowd_period=3, slowd_matype=0)

apple['STOCHFk'], apple['STOCHFd'] = ta.STOCHF(apple['High'], apple['Low'], apple['Close'], fastk_period=5, fastd_period=3, fastd_matype=0)
apple['STOCHRSIk'], apple['STOCHRSId'] = ta.STOCHRSI(apple['Close'], timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0)
apple['TRIX']= ta.TRIX(apple['Close'], timeperiod=30)
apple['ULTOSC'] = ta.ULTOSC(apple['High'], apple['Low'], apple['Close'], timeperiod1=7, timeperiod2=14, timeperiod3=28)

apple['upperband'], apple['middleband'], apple['lowerband'] = ta.BBANDS(apple['Close'], timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)
apple['DEMA'] = ta.DEMA(apple['Close'], timeperiod=30)
apple['EMA']= ta.EMA(apple['Close'], timeperiod=30)
apple['HT_TRENDLINE'] = ta.HT_TRENDLINE(apple['Close'])
apple['KAMA'] = ta.KAMA(apple['Close'], timeperiod=30)
apple['MA'] = ta.MA(apple['Close'], timeperiod=30, matype=0)
apple['MIDPOINT'] = ta.MIDPOINT(apple['Close'], timeperiod=14)
apple['MIDPRICE'] = ta.MIDPRICE(apple['High'], apple['Low'], timeperiod=14)
apple['SAR'] = ta.SAR(apple['High'], apple['Low'], acceleration=0, maximum=0)
apple['SMA'] = ta.SMA(apple['High'], timeperiod=30)
apple['T3'] = ta.T3(apple['Close'], timeperiod=30, vfactor=0)
apple['TEMA'] = ta.TEMA(apple['Close'], timeperiod=30)
apple['TRIMA']= ta.TRIMA(apple['Close'], timeperiod=30)
apple['WMA'] = ta.WMA(apple['Close'], timeperiod=30)
apple['ATR'] = ta.ATR(apple['High'], apple['Low'], apple['Close'], timeperiod=14)
apple['NATR']= ta.NATR(apple['High'], apple['Low'], apple['Close'], timeperiod=14)
apple['TRANG'] = ta.TRANGE(apple['High'], apple['Low'], apple['Close'])
apple['AVGPRICE']= ta.AVGPRICE(apple['Open'],apple['High'], apple['Low'],apple['Close'])
apple['MEDPRICE'] = ta.MEDPRICE(apple['High'], apple['Low'])
apple['TYPPRICE'] = ta.TYPPRICE(apple['High'], apple['Low'], apple['Close'])
apple['WCLPRICE'] = ta.WCLPRICE(apple['High'], apple['Low'], apple['Close'])
apple['HT_DCPERIOD'] = ta.HT_DCPERIOD(apple['Close'])
apple['HT_DCPHASE'] = ta.HT_DCPHASE(apple['Close'])
apple['inphase'], apple['quadrature'] = ta.HT_PHASOR(apple['Close'])
apple['sine'], apple['leadsine'] = ta.HT_SINE(apple['Close'])
apple['HT_TRENDMODE'] = ta.HT_TRENDMODE(apple['Close'])

apple['STOCHOSI']
apple=pd.DataFrame(apple)
# applying ffill() method to fill the missing values
apple=apple.ffill(axis = True)
apple[:]

apple['MACD_EMA']

#defining up & down signals
close=apple['Close'].transform(lambda x:x.shift(1)<x)
apple['Prediction']=close*1

#data cleaning
apple=apple.dropna()

apple_X=apple.drop(columns=['Prediction','Date'])
apple_y=apple['Prediction']

# defining train-test data set
X_train = apple_X[:int(apple_X.shape[0]*0.7)]
X_test = apple_X[int(apple_X.shape[0]*0.7):]
y_train = apple_y[:int(apple_X.shape[0]*0.7)]
y_test = apple_y[int(apple_X.shape[0]*0.7):]

#Scaling
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train_std=sc.fit_transform(X_train)
X_test_std=sc.transform(X_test)

#PCA application
from sklearn.decomposition import PCA
pca = PCA(n_components=0.95)
X_train_pca = pca.fit_transform(X_train_std)
X_test_pca=pca.transform(X_test_std)

#training and evaluation random forest
from sklearn.ensemble import RandomForestClassifier
rfr = RandomForestClassifier(n_estimators=200,n_jobs=-1, random_state=0)
rfr.fit(X_train_pca,y_train)
y_pred_rfr=rfr.predict(X_test_pca)
y_pred_rfr

accuracy= accuracy_score(y_test, y_pred_rfr)
print("Accuracy is : ", accuracy)
tn_rf, fp_rf, fn_rf, tp_rf = confusion_matrix(y_test, y_pred_rfr).ravel()
precision_rf=(tp_rf)/(tp_rf+fp_rf)
print("Precision of random Forest is : ",precision_rf)
recall_rf=(tp_rf)/(tp_rf+fn_rf)
print("Recall of Random Forest is : ", recall_rf)
f1_rf=(2*recall_rf*precision_rf)/(precision_rf+recall_rf)
print("F1 Score of Random Forest is : ", f1_rf)
specificity = tn_rf / (tn_rf+fp_rf)
print("Specificity of Random Forest is : ", specificity)
rfr_probs = rfr.predict_proba(X_test_pca)[:, 1]
roc_auc_score(y_test, rfr_probs)
fpr_rfr, tpr_rfr, thresholds_rfr = roc_curve(y_test, rfr_probs)
auc_rfr = auc(fpr_rfr, tpr_rfr)
print("AUC of Random Forest is : ", auc_rfr)

"""**XGBClassifier**"""

#trainning & evaluating xgboost
from xgboost import XGBClassifier
xg = XGBClassifier(n_estimators=200, random_state=0)
xg.fit(X_train_pca, y_train)
y_pred_xg = xg.predict(X_test_pca)
accuracy = accuracy_score(y_test, y_pred_xg)
print("Accuracy of XG Boost Classifier : ", accuracy)
tn_xg, fp_xg, fn_xg, tp_xg = confusion_matrix(y_test, y_pred_xg).ravel()
precision_xg=(tp_xg)/(tp_xg+fp_xg)
print("Precision of XG Boost Classifier is : ",precision_xg)
recall_xg=(tp_xg)/(tp_xg+fn_xg)
print("Recall of XG Boost Classifier is : ", recall_xg)
f1_xg=(2*recall_xg*precision_xg)/(precision_xg+recall_xg)
print("F1 Score of XG Boost Classifier is : ", f1_xg)

specificity = tn_xg / (tn_xg+fp_xg)
print("Specificity of XG Boost Classifier is : ", specificity)

xg_probs = xg.predict_proba(X_test_pca)[:, 1]
roc_auc_score(y_test, xg_probs)
fpr_xg, tpr_xg, thresholds_xg = roc_curve(y_test, xg_probs)
auc_xg = auc(fpr_xg, tpr_xg)
print("AUC of XG Boost Classifier is : ", auc_xg)

"""**** **BaggingClassifier**"""

#training & evaluating baggingclassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier

Bag = BaggingClassifier(n_estimators=200, random_state=0)
Bag.fit(X_train_pca, y_train)
y_pred_Bag = Bag.predict(X_test_pca)
accuracy = accuracy_score(y_test, y_pred_Bag)
print("Accuracy of Bagging Classifier : ", accuracy)
tn_Bag, fp_Bag, fn_Bag, tp_Bag = confusion_matrix(y_test, y_pred_Bag).ravel()
precision_Bag=(tp_Bag)/(tp_Bag+fp_Bag)
print("Precision of Bagging Classifier : ", precision_Bag)
recall_Bag=(tp_Bag)/(tp_Bag+fn_Bag)
print("Recall of Bagging Classifier : ", recall_Bag)
f1_Bag=(2*recall_Bag*precision_Bag)/(precision_Bag+recall_Bag)
print("F1 Score of Bagging Classifier : ", f1_Bag)
specificity = tn_Bag / (tn_Bag+fp_Bag)
print("Specificity of Bagging Classifier : ", specificity)
Bag_probs = Bag.predict_proba(X_test_pca)[:, 1]
roc_auc_score(y_test, Bag_probs)
fpr_Bag, tpr_Bag, thresholds_Bag = roc_curve(y_test, Bag_probs)
auc_Bag = auc(fpr_Bag, tpr_Bag)
print("AUC of Bagging Classifier : ", auc_Bag)

"""**AdaBoostClassifier**"""

#trainning &evaluating adaboost
from sklearn.ensemble import AdaBoostClassifier
ada = AdaBoostClassifier(n_estimators=200, learning_rate=1, random_state=0)
ada.fit(X_train_pca, y_train)
y_pred_ada=ada.predict(X_test_pca)
accuracy = accuracy_score(y_test, y_pred_ada)
print("Accuracy of AdaBoostClassifier : ", accuracy)
tn_ada, fp_ada, fn_ada, tp_ada = confusion_matrix(y_test, y_pred_ada).ravel()
precision_ada=(tp_ada)/(tp_ada+fp_ada)
print("Precision of AdaBoostClassifier : ", precision_ada)
recall_ada=(tp_ada)/(tp_ada+fn_ada)
print("Recall of AdaBoostClassifier : ", recall_ada)
f1_ada=(2*recall_ada*precision_ada)/(precision_ada+recall_ada)
print("F1 Score of AdaBoostClassifier : ", f1_ada)
specificity = tn_ada / (tn_ada+fp_ada)
print("Specificity of AdaBoostClassifier : ", specificity)
ada_probs = ada.predict_proba(X_test_pca)[:, 1]
roc_auc_score(y_test, ada_probs)
fpr_ada, tpr_ada, thresholds_ada = roc_curve(y_test, ada_probs)
auc_ada = auc(fpr_ada, tpr_ada)
print("AUC of AdaBoostClassifier : ", auc_ada)

"""**ExtraTreesClassifier**"""

#trainning &evaluating extratrees
from sklearn.ensemble import ExtraTreesClassifier
et = ExtraTreesClassifier(n_estimators=200, random_state=0)
et.fit(X_train_pca, y_train)
y_pred_et=et.predict(X_test_pca)
accuracy = accuracy_score(y_test, y_pred_et)
print("Accuracy of ExtraTreesClassifier : ", accuracy)
tn_et, fp_et, fn_et, tp_et = confusion_matrix(y_test, y_pred_et).ravel()
precision_et=(tp_et)/(tp_et+fp_et)
print("Precision of ExtraTreesClassifier : ", precision_et)
recall_et=(tp_et)/(tp_et+fn_et)
print("Recall of ExtraTreesClassifier : ", recall_et)
f1_et=(2*recall_et*precision_et)/(precision_et+recall_et)
print("F1 Score of ExtraTreesClassifier : ", f1_et)
specificity = tn_et / (tn_et+fp_et)
print("Specificity of ExtraTreesClassifier : ", specificity)
et_probs = et.predict_proba(X_test_pca)[:, 1]
roc_auc_score(y_test, et_probs)
fpr_et, tpr_et, thresholds_et = roc_curve(y_test, et_probs)
auc_et = auc(fpr_et, tpr_et)
print("AUC of ExtraTreesClassifier : ", auc_et)

"""**Voting Classifier**"""

#trainning &evaluating voting classifier
from sklearn.ensemble import VotingClassifier
vc = VotingClassifier(estimators=[
                          ('rfrr', rfr), ('xgg',xg),
                          ('Bagg', Bag), ('adaa', ada), ('ett',et)],  
                                 
                     voting='soft')
vc.fit(X_train_pca, y_train)
y_pred_vc=vc.predict(X_test_pca)
accuracy = accuracy_score(y_test, y_pred_vc)
print("Accuracy of Voting Classifier : ", accuracy)
tn_vc, fp_vc, fn_vc, tp_vc = confusion_matrix(y_test, y_pred_vc).ravel()
precision_vc=(tp_vc)/(tp_vc+fp_vc)
print("Precision of Voting Classifier : ", precision_vc)
recall_vc=(tp_vc)/(tp_vc+fn_vc)
print("Recall of Voting Classifier : ", recall_vc)
f1_vc=(2*recall_vc*precision_vc)/(precision_vc+recall_vc)
print("F1 Score of Voting Classifier : ", f1_vc)
specificity = tn_vc / (tn_vc+fp_vc)
print("Specificity of Voting Classifier : ", specificity)
vc_probs = vc.predict_proba(X_test_pca)[:, 1]
roc_auc_score(y_test, vc_probs)
fpr_vc, tpr_vc, thresholds_vc = roc_curve(y_test, vc_probs)
auc_vc = auc(fpr_vc, tpr_vc)
print("AUC of Voting Classifier : ", auc_vc)

"""**ROC Curves**"""

#plotting roc curves of the classifiers
plt.plot(fpr_rfr, tpr_rfr, color='y', label='Random_Forest (area = {:.3f})'.format(auc_rfr))
plt.plot(fpr_xg, tpr_xg, color='b', label='XGBoost (area = {:.3f})'.format(auc_xg))
plt.plot(fpr_Bag, tpr_Bag, color='r', label='Bagging_Classifier(area = {:.3f})'.format(auc_Bag))
plt.plot(fpr_ada, tpr_ada, color='g', label='AdaBoost (area = {:.3f})'.format(auc_ada))
plt.plot(fpr_et, tpr_et, color='c', label='Extra_Trees (area = {:.3f})'.format(auc_et))
plt.plot(fpr_vc, tpr_vc, color='m', label='Voting_Classifier (area = {:.3f})'.format(auc_vc))
plt.plot([0, 1], [0, 1], color='darkblue', linestyle='--')
#plt.xlim([0.0, 1.0])
#plt.ylim([0.0, 1.0])
plt.xlabel('False positive rate')
plt.ylabel('True positive rate')
#plt.title('ROC curve')
plt.legend(loc='best')
plt.show()

"""**LSTM**"""

#importing the packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
from sklearn.preprocessing import MinMaxScaler
#used for setting the output figure size
rcParams['figure.figsize'] = 20,10
#to normalize the given input data
scaler = MinMaxScaler(feature_range=(0, 1))
#to read input data set (place the file name inside  ' ') as shown below
todataframe = apple
#to print the first few data in the data set
todataframe.head(10)

todataframe['Date'] = pd.to_datetime(todataframe.Date,format='%m/%d/%Y')
todataframe.index = todataframe['Date']
plt.figure(figsize=(16,8))
plt.plot(todataframe['Close'], label='Closing Price')

# Extracting the closing prices of each day
FullData=apple[['Close']].values
print(FullData[0:10])
 
# Feature Scaling for fast training of neural networks
from sklearn.preprocessing import StandardScaler, MinMaxScaler
 
# Choosing between Standardization or normalization
#sc = StandardScaler()
sc=MinMaxScaler()
 
DataScaler = sc.fit(FullData)
X=DataScaler.transform(FullData)
#X=FullData
 
print('### After Normalization ###')
X[0:5]

"""**Preparing the data for LSTM**"""

#split into samples
X_samples = list()
y_samples = list()

NumerOfRows = len(X)
TimeSteps=10  # next day's Price Prediction is based on last how many past day's prices

# Iterate thru the values to create combinations
for i in range(TimeSteps , NumerOfRows , 1):
    x_sample = X[i-TimeSteps:i]
    y_sample = X[i]
    X_samples.append(x_sample)
    y_samples.append(y_sample)

################################################
# Reshape the Input as a 3D (number of samples, Time Steps, Features)
X_data=np.array(X_samples)
X_data=X_data.reshape(X_data.shape[0],X_data.shape[1], 1)
print('\n#### Input Data shape ####')
print(X_data.shape)

# We do not reshape y as a 3D data  as it is supposed to be a single column only
y_data=np.array(y_samples)
y_data=y_data.reshape(y_data.shape[0], 1)
print('\n#### Output Data shape ####')
print(y_data.shape)

"""**Visualizing the input and output data for LSTM**"""

# Visualizing the input and output being sent to the LSTM model
for inp, out in zip(X_train[0:2], y_train[0:2]):
    print(inp,'--', out)

"""**Creating the Deep Learning LSTM model**"""

#split into samples
X_samples = list()
y_samples = list()

NumerOfRows = len(X)
TimeSteps=10  # next day's Price Prediction is based on last how many past day's prices

# Iterate thru the values to create combinations
for i in range(TimeSteps , NumerOfRows , 1):
    x_sample = X[i-TimeSteps:i]
    y_sample = X[i]
    X_samples.append(x_sample)
    y_samples.append(y_sample)

################################################
# Reshape the Input as a 3D (number of samples, Time Steps, Features)
X_data=np.array(X_samples)
X_data=X_data.reshape(X_data.shape[0],X_data.shape[1], 1)
print('\n#### Input Data shape ####')
print(X_data.shape)

# We do not reshape y as a 3D data  as it is supposed to be a single column only
y_data=np.array(y_samples)
y_data=y_data.reshape(y_data.shape[0], 1)
print('\n#### Output Data shape ####')
print(y_data.shape)

# Choosing the number of testing data records
TestingRecords=980
 
# Splitting the data into train and test
X_train=X_data[:-TestingRecords]
X_test=X_data[-TestingRecords:]
y_train=y_data[:-TestingRecords]
y_test=y_data[-TestingRecords:]
 
############################################
 
# Printing the shape of training and testing
print('\n#### Training Data shape ####')
print(X_train.shape)
print(y_train.shape)
print('\n#### Testing Data shape ####')
print(X_test.shape)
print(y_test.shape)

# Defining Input shapes for LSTM
TimeSteps=X_train.shape[1]
TotalFeatures=X_train.shape[2]
print("Number of TimeSteps:", TimeSteps)
print("Number of Features:", TotalFeatures)

# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
 
# Initialising the RNN
regressor = Sequential()
 
# Adding the First input hidden layer and the LSTM layer
# return_sequences = True, means the output of every time step to be shared with hidden next layer
regressor.add(LSTM(units = 10, activation = 'relu', input_shape = (TimeSteps, TotalFeatures), return_sequences=True))
 
# Adding the Second Second hidden layer and the LSTM layer
regressor.add(LSTM(units = 5, activation = 'relu', input_shape = (TimeSteps, TotalFeatures), return_sequences=True))
 
# Adding the Second Third hidden layer and the LSTM layer
regressor.add(LSTM(units = 5, activation = 'relu', return_sequences=False ))
 
 
# Adding the output layer
regressor.add(Dense(units = 1))
 
# Compiling the RNN
regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')
 
##################################################
 
import time
# Measuring the time taken by the model to train
StartTime=time.time()
 
# Fitting the RNN to the Training set
regressor.fit(X_train, y_train, batch_size = 5, epochs = 100)
 
EndTime=time.time()
print("## Total Time Taken: ", round((EndTime-StartTime)/60), 'Minutes ##')

print(regressor.summary())

"""**Measuring the accuracy of the model on testing data**"""

# Making predictions on test data

predicted_Price = regressor.predict(X_test)
predicted_Price = DataScaler.inverse_transform(predicted_Price)

 # Getting the original price values for testing data
orig=y_test
orig=DataScaler.inverse_transform(y_test)
 
# Accuracy of the predictions
print('Accuracy:', 100 - (100*(abs(orig-predicted_Price)/orig)).mean())
 
# Visualising the results
import matplotlib.pyplot as plt
 
plt.plot(predicted_Price, color = 'green', label = 'Predicted Volume')
plt.plot(orig, color = 'red', label = 'Original Volume')
 
plt.title('Stock Price Predictions')
todataframe['Date'] = pd.to_datetime(todataframe.Date,format='%Y-%m-%d')
todataframe.index = todataframe['Date']
plt.xlabel('Trading Date')
plt.xticks(range(TestingRecords), apple.tail(TestingRecords)['Date'])
plt.ylabel('Stock Price')
 
plt.legend()
fig=plt.gcf()
fig.set_figwidth(20)
fig.set_figheight(6)
plt.show()

"""**Visualizing the predictions for full data**"""

# Generating predictions on full data
TrainPredictions=DataScaler.inverse_transform(regressor.predict(X_train))
TestPredictions=DataScaler.inverse_transform(regressor.predict(X_test))
 
FullDataPredictions=np.append(TrainPredictions, TestPredictions)
FullDataOrig=FullData[TimeSteps:]
 
# plotting the full data
plt.plot(FullDataPredictions, color = 'green', label = 'Predicted Price')
plt.plot(FullDataOrig , color = 'red', label = 'Original Price')
 
 
plt.title('Stock Price Predictions')
plt.xlabel('Trading Date')
plt.ylabel('Stock Price')
plt.legend()
fig=plt.gcf()
fig.set_figwidth(20)
fig.set_figheight(8)
plt.show()

"""**Data Preparation for Multi Step LSTM**"""

# Considering the Full Data again which we extracted above
# Printing the last 10 values
print('Original Prices')
print(FullData[-10:])
 
print('###################')
 
# Printing last 10 values of the scaled data which we have created above for the last model
# Here I am changing the shape of the data to one dimensional array because
# for Multi step data preparation we need to X input in this fashion
X=X.reshape(X.shape[0],)
print('Scaled Prices')
print(X[-10:])

"""**Measuring the Accuracy of the model on testing data**"""

# Making predictions on test data
predicted_Price = regressor.predict(X_test)
predicted_Price = DataScaler.inverse_transform(predicted_Price)
print('#### Predicted Prices ####')
print(predicted_Price)
 
# Getting the original price values for testing data
orig=y_test
orig=DataScaler.inverse_transform(y_test)
print('\n#### Original Prices ####')
print(orig)

"""**Making predictions for the next 5 days**"""

# Making predictions on test data
from array import array
import numpy as np
Last10DaysPrices=np.array([161.79,162.88,156.8,156.57,163.64,157.65,157.96,159.48,166.02,156.77])
 
# Reshaping the data to (-1,1 )because its a single entry
Last10DaysPrices=Last10DaysPrices.reshape(-1, 1)
 
# Scaling the data on the same level on which model was trained
X_test=DataScaler.transform(Last10DaysPrices)
 
NumberofSamples=1
TimeSteps=X_test.shape[0]
NumberofFeatures=X_test.shape[1]
# Reshaping the data as 3D input
X_test=X_test.reshape(NumberofSamples,TimeSteps,NumberofFeatures)
 
# Generating the predictions for next 5 days
Next5DaysPrice = regressor.predict(X_test)
 
# Generating the prices in original scale
Next5DaysPrice = DataScaler.inverse_transform(Next5DaysPrice)
Next5DaysPrice