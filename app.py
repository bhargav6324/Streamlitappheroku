# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 21:02:57 2023

@author: bharg
"""
import numpy as np
import streamlit as st

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import pickle

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

file_id = '1pQesHyqFKNQgN3EdqN3G_ZVZMfpLg9lx'
downloaded = drive.CreateFile({'id': file_id})
downloaded.GetContentFile('trained_model.sav')

loaded_model = pickle.load(open('trained_model.sav', 'rb'))



#creating a function for prediction
def cancer_prediction(input_data):
    
    # Replace empty strings with 0
    input_data = [0 if x == '' else x for x in input_data]

    
    input_data_as_numpy_array = np.asarray(input_data, dtype=np.float64)

    # reshape the numpy array
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)

    if(prediction[0] == 0):
        return 'The Breast Cancer is Malignant'
    else:
        return 'The Breast Cancer is Benign'


def main():
    
    #giving a title 
    st.title('Breast Cancer Prediction Web App')
    
    
    #getting the input from  user
    
    radius_mean = st.text_input('Enter the Radius Mean')
    texture_mean = st.text_input('Enter the Texture Mean')
    perimeter_mean = st.text_input('Enter the Perimeter Mean')
    area_mean = st.text_input('Enter the Area Mean')
    smoothness_mean = st.text_input('Enter the Smoothness Mean')
    compactness_mean = st.text_input('Enter the Compactness Mean')
    concavity_mean = st.text_input('Enter the concavity Mean')
    concave_points_mean = st.text_input('Enter the Concave Points Mean')
    symmetry_mean = st.text_input('Enter the Symmetry Mean')
    fractal_dimension_mean = st.text_input('Enter the fractal dimension mean')
    radius_se = st.text_input('Standard Error in radius')
    texture_se = st.text_input('Standard Error in Texture')
    perimeter_se = st.text_input('Standard Error in Perimeter')
    area_se = st.text_input('Standard Error in Area')
    smoothness_se = st.text_input('Standard Error in Smoothness')
    compactness_se = st.text_input('Standard Error in Compactness')
    concavity_se = st.text_input('Standard Error in Concavity')
    concave_points_se = st.text_input('Standard Error in Concave points')
    symmetry_se = st.text_input('Standard Error in Symmetry')
    fractal_dimension_se = st.text_input('Standard Error in Fractal Dimension')
    radius_worst = st.text_input('worst value for mean of distances from center to points on the perimeter')
    texture_worst = st.text_input('Enter Texture worst')
    perimeter_worst = st.text_input('Enter Perimeter worst')
    area_worst = st.text_input('Enter Area worst')
    smoothness_worst = st.text_input('Enter smoothness worst')
    compactness_worst = st.text_input('Enter Compactness worst')
    concavity_worst = st.text_input('Enter Concavity worst')
    concave_points_worst = st.text_input('Concave Points worst')
    symmetry_worst = st.text_input('Symmetry Points worst')
    fractal_dimension_worst = st.text_input('Fractal Dimension Points worst')
    
    #code for prediction 
    diagnosis = ''
    
    #Creating button for prediction

    
    if st.button("Breast Cancer Test Result"):
      diagnosis = cancer_prediction([radius_mean ,texture_mean ,perimeter_mean , area_mean , smoothness_mean ,compactness_mean,concavity_mean,concave_points_mean,symmetry_mean,fractal_dimension_mean,radius_se,texture_se,perimeter_se,area_se,smoothness_se,compactness_se,concavity_se,concave_points_se,symmetry_se,fractal_dimension_se,radius_worst,texture_worst,perimeter_worst,area_worst,smoothness_worst,compactness_worst,concavity_worst,concave_points_worst,symmetry_worst,fractal_dimension_worst])
  
    st.success(diagnosis)
    
    
    
if __name__ == '__main__':
    main()
    
