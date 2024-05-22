import pickle
import streamlit as st
import numpy as np
from streamlit_option_menu import option_menu 
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt


# loading the saved models

diabetes_model = pickle.load(open("./models/diabetes_model.sav",'rb'))
parkinsons_model = pickle.load(open("./models/parkinsons_model.sav",'rb'))
lung_cancer_model = pickle.load(open("./models/lung_cancer.sav",'rb'))


# sidebar navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System', 
                           [ 'Diabetes Prediction',
                            'Parkinson\'s Prediction',
                            'Stroke Prediction', 'Autism Prediction' , 'Depression Prediction', 'Lung Cancer Prediction', 'Covid Prediction'],
                           icons=['heart','activity','person','gender-female'],
                           default_index=0)





# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
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
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
        
    # code for prediction
    diab_diagnosis=''
    
    # create a button for prediction
    
    if st.button('Diabetes Test Result'):
        if not all([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]):
            st.warning("Please fill in all the fields.")
        else:
            diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
            
            if (diab_prediction[0] == 1):
              diab_diagnosis = 'The person is diabetic'
            else:
              diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)  
  

    


# Parkinsons Prediction Page  
if (selected == 'Parkinson\'s Prediction'):    
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP: Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP: Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP: Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP: Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP: Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP: RAP')
        
    with col2:
        PPQ = st.text_input('MDVP: PPQ')
        
    with col3:
        DDP = st.text_input('Jitter: DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP: Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP: Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer: APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer: APQ5')
        
    with col3:
        APQ = st.text_input('MDVP: APQ')
        
    with col4:
        DDA = st.text_input('Shimmer: DDA')
        
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
        if not all([fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]):
            st.warning("Please fill in all the fields.")
        else:
            parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
            
            if (parkinsons_prediction[0] == 1):
              parkinsons_diagnosis = "The person has Parkinson's disease"
            else:
              parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)    


# Autism

if selected == 'Autism Prediction':
    st.title('Autism Prediction using ML')
    col1, col2, col3, col4 = st.columns(4)
    
    model1 = pickle.load(open('./models/logreg.pkl', 'rb'))

    def find_asd(res):
        if res == 1:
            return 'The person has Autism Spectrum Disorder'
        else:
            return 'The person does not have Autism Spectrum Disorder'
        
    ethnicities = ["Asian", "Black", "Hispanic", "Latino", "Middle Eastern", "Others", "Pasifika", "South Asian", "Turkish", "White-European"]
    relations = ["Health Care Professional", "Others", "Parent", "Relative", "Self"]
    genders = ["Female", "Male"]

    a1 = st.selectbox("A1 Score", [0, 1])
    a2 = st.selectbox("A2 Score", [0, 1])
    a3 = st.selectbox("A3 Score", [0, 1])
    a4 = st.selectbox("A4 Score", [0, 1])
    a5 = st.selectbox("A5 Score", [0, 1])
    a6 = st.selectbox("A6 Score", [0, 1])
    a7 = st.selectbox("A7 Score", [0, 1])
    a8 = st.selectbox("A8 Score", [0, 1])
    a9 = st.selectbox("A9 Score", [0, 1])
    a10 = st.selectbox("A10 Score", [0, 1])
    age = st.number_input("Age")
    gender = st.selectbox("Gender", genders)
    ethnicity = st.selectbox("Ethnicity", ethnicities)
    jaundice = st.selectbox("Jaundice", [0, 1])
    autism = st.selectbox("Autism", [0, 1])
    used_app_before = st.selectbox("Used App Before", [0, 1])
    result = st.number_input("Result")
    relation = st.selectbox("Relation", relations)

    if st.button("Detect"):
        gender = genders.index(gender)
        ethnicity = ethnicities.index(ethnicity)
        relation = relations.index(relation)
        test = np.array([[a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, age, gender, ethnicity, jaundice, autism, used_app_before, result, relation]])
        res1 = model1.predict(test)
        print(res1)
        result1 = find_asd(res1[0])
        st.success(" " + result1)

if selected == 'Stroke Prediction':

    st.title('Stroke Prediction using ML')
    model_stroke = pickle.load(open('./models/model_stroke.sav', 'rb'))
    col1, col2 = st.columns(2)

    with col1:
        gender_select = st.selectbox('Gender', options=['Female', 'Male'])
        gender = 1 if gender_select == 'Male' else 0
    
    with col2:
        age = st.number_input('Age', 5, 100)

    with col1:
        hypertension_select = st.selectbox('Hypertension', options=['No', 'Yes'])
        hypertension = 1 if hypertension_select == 'Yes' else 0

    with col2:
        heart_disease_select = st.selectbox('Heart Disease', options=['No', 'Yes'])
        heart_disease = 1 if heart_disease_select == 'Yes' else 0

    with col1:
        ever_married_select = st.selectbox('Ever Married', options=['No', 'Yes'])
        ever_married = 1 if ever_married_select == 'Yes' else 0

    with col2:
        residence_select = st.selectbox('Residence Type', options=['Urban', 'Rural'])
        Residence_type = 1 if residence_select == 'Urban' else 0

    with col1:
        avg_glucose_level = st.number_input('Glucose', min_value=50.0, max_value=300.0, step=0.1)
        
    with col2:
        bmi = st.number_input('Bmi',  min_value=10.0, max_value=100.0, step=0.1)

    with col1:
        smoking_status_select = st.selectbox('Smoking Status', options=['No', 'Yes', 'Unknown', 'formerly smoked'])
        smoking_status = 1 if smoking_status_select == 'Yes' else 0

    govt_job = 0
    never_worked = 0
    private = 0
    self_employed = 0
    children = 0

    with col2:
        selected_work = st.selectbox('Select Work:', options=['Government', 'Never Worked', 'Private', 'Self Employed', 'Children'])
        
    if selected_work == 'Government':
        govt_job = 1
    elif selected_work == 'Never Worked':
        never_worked = 1
    elif selected_work == 'Private':
        private = 1
    elif selected_work == 'Self Employed':
        self_employed = 1
    else:
        children = 1

    stroke_pred = None
    
    if st.button('Stroke Prediction'):
        stroke_pred = model_stroke.predict([[gender, age, hypertension, heart_disease, ever_married, Residence_type, avg_glucose_level, bmi, smoking_status, govt_job, never_worked, private, self_employed, children]])
    
    if stroke_pred is not None:
        if (stroke_pred)[0] == 1:
            stroke_diag = 'you had a stroke'
            st.error(stroke_diag)
        else:
            stroke_diag = "you didn't have a stroke"
            st.success(stroke_diag)

if selected == 'Depression Prediction':
    st.title('Depression Prediction using ML')
    model_depression = pickle.load(open('./models/bagging_model1.pickle', 'rb'))

    q1 = st.selectbox('Little interest or pleasure in doing things?', ['Not at all', 'Several Days','More than half the days','Nearly Everyday'])
    q2 = st.selectbox('Feeling down, depressed, or hopeless?', ['Not at all', 'Several Days','More than half the days','Nearly Everyday'])
    q3 = st.selectbox('Trouble falling or staying asleep, or sleeping too much?', ['Not at all', 'Several Days','More than half the days','Nearly Everyday'])
    q4 = st.selectbox('Feeling tired or having little energy?', ['Not at all', 'Several Days','More than half the days','Nearly Everyday'])
    q5 = st.selectbox('Poor appetite or overeating?', ['Not at all', 'Several Days','More than half the days','Nearly Everyday'])
    q6 = st.selectbox('Feeling bad about yourself - or that you are a failure or have let yourself or your family down?', ['Not at all', 'Several Days','More than half the days','Nearly Everyday'])
    q7 = st.selectbox('Trouble concentrating on things, such as reading the newspaper or watching television?', ['Not at all', 'Several Days','More than half the days','Nearly Everyday'])
    q8 = st.selectbox('Moving or speaking so slowly that other people could have noticed? Or the opposite - being so fidgety or restless that you have been moving around a lot more than usual?', ['Not at all', 'Several Days','More than half the days','Nearly Everyday'])
    q9 = st.selectbox('Thoughts that you would be better off dead, or of hurting yourself in some way?', ['Not at all', 'Several Days','More than half the days','Nearly Everyday'])
    
    Q1 = 0 if q1 == 'More than half the days' else 1 if q1 == 'Nearly Everyday' else 2 if q1 == 'Not at all' else 3
    Q2 = 0 if q2 == 'More than half the days' else 1 if q1 == 'Nearly Everyday' else 2 if q1 == 'Not at all' else 3
    Q3 = 0 if q3 == 'More than half the days' else 1 if q1 == 'Nearly Everyday' else 2 if q1 == 'Not at all' else 3
    Q4 = 0 if q4 == 'More than half the days' else 1 if q1 == 'Nearly Everyday' else 2 if q1 == 'Not at all' else 3
    Q5 = 0 if q5 == 'More than half the days' else 1 if q1 == 'Nearly Everyday' else 2 if q1 == 'Not at all' else 3
    Q6 = 0 if q6 == 'More than half the days' else 1 if q1 == 'Nearly Everyday' else 2 if q1 == 'Not at all' else 3
    Q7 = 0 if q7 == 'More than half the days' else 1 if q1 == 'Nearly Everyday' else 2 if q1 == 'Not at all' else 3
    Q8 = 0 if q8 == 'More than half the days' else 1 if q1 == 'Nearly Everyday' else 2 if q1 == 'Not at all' else 3
    Q9 = 0 if q9 == 'More than half the days' else 1 if q1 == 'Nearly Everyday' else 2 if q1 == 'Not at all' else 3

    attrition = ''

    if st.button('Depression Prediction Result'):
        input_data_as_numpy_array = np.asarray([Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9])
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

        prediction = model_depression.predict(input_data_reshaped)
        if(prediction[0] == 0):
            attrition = 'mild depression'
        elif(prediction[0] == 1):
            attrition = 'moderate depression'
        elif(prediction[0] == 2):
            attrition = 'moderately severe depression'
        elif(prediction[0] == 3):
            attrition = 'severe depression'
        else:
            attrition = 'Severe depression'

    st.success(attrition)

if selected == 'Lung Cancer Prediction':
    st.title('Lung Cancer Prediction using ML')
    col1, col2, col3 = st.columns (3)
    
    with col1:
        GENDER = st.number_input('1 = Male, 2 = Female')
    with col1:
        AGE = st.number_input('Age')
    with col1:
        SMOKING = st.number_input('SMOKING ? 1 = NO, 2 = YES')
    with col1:
        YELLOW_FINGERS = st.number_input ('YELLOW FINGERS ? 1 = NO, 2 = YES')
    with col1:
        ANXIETY = st.number_input('ANXIETY ?  1 = NO, 2 = YES')
    with col2:
        PEER_PRESSURE = st.number_input ('PEER PRESSURE ? 1 = NO, 2 = YES')
    with col2:
        CHRONIC_DISEASE = st.number_input ( 'CHRONIC_DISEASE ? 1 = NO, 2 = YES')
    with col2:
        FATIGUE = st.number_input ('FATIGUE ? 1 = NO, 2 = YES')
    with col2:
        ALLERGY = st.number_input ('ALLERGY ? 1 = NO, 2 = YES')
    with col2:
        WHEEZING = st.number_input ('WHEEZING ? 1 = NO, 2 = YES')
    with col3:
        ALCOHOL_CONSUMING = st.number_input ('ALCOHOL CONSUMING ? 1 = NO, 2 = YES')
    with col3:
        COUGHING = st.number_input ('COUGHING ? 1 = NO, 2 = YES')
    with col3:
        SHORTNESS_OF_BREATH = st.number_input ('SHORTNESS OF BREATH ? 1 = NO, 2 = YES')
    with col3:
        SWALLOWING_DIFFICULTY = st.number_input ('SWALLOWING DIFFICULTY ? 1 = NO, 2 = YES')
    with col3:
        CHEST_PAIN = st.number_input ('CHEST PAIN ? 1 = NO, 2 = YES')
        
    cancer_diagnosis =''
    
    if st.button('Prediction of Lung Cancer Disease'):
        cancer_prediction = lung_cancer_model.predict([[GENDER,AGE,SMOKING,YELLOW_FINGERS,ANXIETY,PEER_PRESSURE,CHRONIC_DISEASE,FATIGUE ,ALLERGY ,WHEEZING,ALCOHOL_CONSUMING,COUGHING,SHORTNESS_OF_BREATH,SWALLOWING_DIFFICULTY,CHEST_PAIN]])
        if (cancer_prediction [0]==1):
            cancer_diagnosis = 'The patient does not have lung cancer.'
        else:
            cancer_diagnosis = 'The patient has lung cancer.'
        
    st.success(cancer_diagnosis)