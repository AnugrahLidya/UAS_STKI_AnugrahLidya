# -*- coding: utf-8 -*-
"""Diabetes.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jeTGe4CBUDYLmX_h_N-MivwN9Xo1Uqae
"""

#1. Menentukan Library yang digunakan
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

#2. Load Dataset
diabetes_dataset = pd.read_csv('diabetes.csv')

diabetes_dataset.head()

diabetes_dataset.shape

diabetes_dataset['Outcome'].value_counts()

#Memisahkan data dan label
X = diabetes_dataset.drop(columns='Outcome', axis=1)
Y = diabetes_dataset['Outcome']

print(X)

print(Y)

#Memisahkan data training dan data testing
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

#Membangun model menggunakan SVM
classifier = svm.SVC(kernel='linear')

classifier.fit(X_train, Y_train)

#Membuat model evaluasi untuk mengukur tingkat akurasi
X_train_prediction = classifier.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
print('Akurasi data training adalah = ', training_data_accuracy)

X_test_prediction = classifier.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print('Akurasi data testing adalah = ', test_data_accuracy)

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# Hitung confusion matrix
cm = confusion_matrix(Y_test, X_test_prediction)

# Tampilkan confusion matrix
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=classifier.classes_)
disp.plot()

from google.colab import drive
drive.mount('/content/drive')

#Membuat model prediksi
input_data = (6, 148, 72, 35, 0, 33.6, 0.627, 50)

input_data_as_numpy_array = np.array(input_data)
input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

# Initialize the StandardScaler and fit it to the training data (X)
scaler = StandardScaler()
scaler.fit(X) # Fit the scaler to your training data

std_data = scaler.transform(input_data_reshaped) # Now you can use transform
print(std_data)

prediction = classifier.predict(std_data)
print(prediction)

if (prediction[0] == 0):
    print('Pasien Tidak Terkena Diabetes')
else:
    print('Pasien Terkena Diabetes')

import pickle
filename = 'diabetes_model.sav'
pickle.dump(classifier, open(filename, 'wb'))