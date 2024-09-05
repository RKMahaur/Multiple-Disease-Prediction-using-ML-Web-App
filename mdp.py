# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 11:39:29 2024

@author: 91981
"""
import numpy as np
import pickle
import streamlit as st
import streamlit_option_menu 

# loading the model and scaler

diabetes_model = pickle.load(open('diabetes_model.pkl','rb'))
diabetes_scaler = pickle.load(open('diabetes_scaler.pkl','rb'))


heart_model = pickle.load(open('heart_model.pkl','rb'))


parkinsons_model = pickle.load(open('parkinsons_model.pkl','rb'))
parkinsons_scaler = pickle.load(open('parkinsons_scaler.pkl','rb'))


# sidebar for navigate

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           menu_icon='hospital-fill',
                           icons = ['activity','heart','person'],
                           default_index = 0)
    
# Diabetes Prediction Page

if(selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    # getting the input data from the user
    # columns for input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnencies = st.text_input('Number of Pregnencies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree function value')
    with col2:
        Age = st.text_input('Age of the Person')
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    if st.button('Diabetes Test Result'):
        
        user_input = [Pregnencies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        
        user_input = [float(x) for x in user_input]
        
        diab_prediction = diabetes_model.predict([user_input])
        
        if(diab_prediction[0]==1):
            diab_diagnosis = 'The person is Diabetic.'
            
        else:
            diab_diagnosis = 'The person is Not Diabetic.'
            
    st.success(diab_diagnosis)
    
if(selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    # getting the input data from the user
    # columns for input fields
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.text_input('Age of the Person')
    with col2:
        sex = st.text_input('Sex of the Person')
    with col1:
        cp = st.text_input('Chest Pain type')
    with col2:
        trestbps = st.text_input('Resting Blood Pressure value')
    with col1:
        chol = st.text_input('Serum Cholestoral value(mg/dl)')
    with col2:
        fbs = st.text_input('Fasting Blood Sugar value(>120 mg/dl)')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results(0,1,2)')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved value')
    with col1:
        exang = st.text_input('Exercise Induced angina')
    with col2:
        oldpeak = st.text_input('Oldpeak = ST depression induced by exercise relative to rest')
    with col1:
        slope = st.text_input('Slope of Peak Exercise ST segment')
    with col2:
        ca = st.text_input('Number of Major vessels (0-3) colored by flourosopy')
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_model.predict([user_input])

        if(heart_prediction[0]==1):
            heart_diagnosis = 'The person is having Heart Disease.'
            
        else:
            heart_diagnosis = 'The person does not have any Heart Disease.'
            
    st.success(heart_diagnosis)
    
if(selected == 'Parkinsons Prediction'):

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    with col1:
        RAP = st.text_input('MDVP:RAP')
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
    with col3:
        DDP = st.text_input('Jitter:DDP')
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
    with col3:
        APQ = st.text_input('MDVP:APQ')
    with col4:
        DDA = st.text_input('Shimmer:DDA')
    with col5:
        NHR = st.text_input('NHR')
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    with col4:
        spread1 = st.text_input('spread1')
    with col5:
        spread2 = st.text_input('spread2')
    with col1:
        D2 = st.text_input('D2')
    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]
        
        input_data_as_numpy_array = np.asarray(user_input)

        # reshape the numpy array
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

        # standardize the data
        std_data = parkinsons_scaler.transform(input_data_reshaped)

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease."
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease."
            
    st.success(parkinsons_diagnosis)
