from grpc import GenericRpcHandler
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import r2_score as scorer
from sklearn.model_selection import train_test_split as tts
from matplotlib import pyplot as mt

################################################################ DEFINITONS ######################################################################
def gender():
    global gender_
    gender_ = input('Please type your gender(1  for male, 2 for female)')
    gender_ = int(gender_)
    if gender_ != 1 and gender_ !=2:
        print('1 for male, 2 for female !!!')
        gender()
def pollution():
    global pollution_
    pollution_ = input('Air Pollution(1 for low, 8 for high)')
    pollution_ = int(pollution_)

    if not 1 <= pollution_ <= 8 :
        print('Please type a number between 1 and 8 according to explaination given!!!')
        pollution()
def alcohol():
    global alcohol_
    alcohol_ = input('Alcohol Usage(1 for low, 8 for high)')
    alcohol_ = int(alcohol_)

    if not 1 <= alcohol_ <= 8:
        print('Please type a number between 1 and 8 according to explaination given!!!')
        alcohol()     
def allergy():
    global allergy_
    allergy_ = input('Dust Allergy(1 for low, 8 for high)')
    allergy_ = int(allergy_)

    if not 1 <= allergy_ <= 8:
        print('Please type a number between 1 and 8 according to explaination given!!!')
        allergy()
def hazard():
    global hazard_
    hazard_ = input('Occupational Hazards(1 for low, 8 for high)')
    hazard_ = int(hazard_)

    if not 1 <= hazard_ <= 8:
        print('Please type a number between 1 and 8 according to explaination given!!!')
        hazard()
def genetic():
    global genetic_
    genetic_ = input('Genetic risk(1 for low, 8 for high)')
    genetic_ = int(genetic_)

    if not 1 <= genetic_ <= 8:
        print('Please type a number between 1 and 8 according to explaination given!!!')
        genetic()
def chronic():
    global chronic_
    chronic_ = input('Chronic Lung Disease(1 for low, 8 for high)')
    chronic_ = int(chronic_)

    if not 1 <= chronic_ <= 8:
        print('Please type a number between 1 and 8 according to explaination given!!!')
        chronic()
def diet():
    global diet_
    diet_ = input('Balanced Diet(1 for poor, 8 for nutricious)')
    diet_ = int(diet_)

    if not  1 <= diet_ <= 8:
        print('Please type a number between 1 and 8 according to explaination given!!!')
        diet()
def obesity():
    global obesity_
    obesity_ = input('Obesity(1 for low, 8 for high)')
    obesity_ = int(obesity_)

    if not 1 <= obesity_ <= 8:
        print('Please type a number between 1 and 8 according to explaination given!!!')
        obesity()
def smoking():
    global smoking_
    smoking_ = input('Smoking(1 for low, 8 for high)')
    smoking_ = int(smoking_)

    if not 1 <= smoking_ <= 8:
        print('Please type a number between 1 and 8 according to explaination given!!!')
        smoking()
def passive():
    global passive_
    passive_ = input('Passive Smoking(1 for low, 8 for high)')
    passive_ = int(passive_)

    if not 1 <= passive_ <= 8:
        print('Please type a number between 1 and 8 according to explaination given!!!')
        passive()
def chest():
    global chest_
    chest_ = input('Chest Pain(1 for low, 8 for high)')
    chest_ = int(chest_)

    if not 1 <= chest_ <= 8:
        print('Please type a number between 1 and 8 according to explaination given!!!')
        chest()
def cough():
    global cough_
    cough_ = input('Coughing of Blood(1 for low, 8 for high)')
    cough_ = int(cough_)

    if not 1 <= cough_ <= 8:
        print('Please type a number between 1 and 8 according to explaination given!!!')
        cough()
def fatigue():
    global fatigue_
    fatigue_ = input('Fatigue(1 for low, 8 for high)')
    fatigue_ = int(fatigue_)

    if not 1 <= fatigue_ <= 8:
        print('Please type a number between 1 and 8 according to explaination given!!!')
        fatigue()
def weight():
    global weight_
    weight_ = input('Weight Loss(1 for low, 8 for high)')
    weight_ = int(weight_)

    if not 1 <= weight_ <= 8:
        print('Please type a number between 1 and 8 according to explaination given!!!')
        weight()
def short():
    global short_
    short_ = input('Shortness of Breath(1 for low, 8 for high)')
    short_ = int(short_)
    
    if not 1 <= short_ <= 8:
        print('Please type a number between 1 and 8 according to explaination given!!!')
        short()
def wheezing():
    global wheezing_
    wheezing_ = input('Wheezing(1 for low, 8 for high)')
    wheezing_ = int(wheezing_)

    if not 1 <= wheezing_ <= 8:
        print('Please type a number between 1 and 8 according to explaination given!!!')
        wheezing()    
def swallow():
    global swallow_
    swallow_ = input('Swallowing Diffculty(1 for low, 8 for high)')
    swallow_ = int(swallow_)
    
    if not 1 <= swallow_ <= 8:
        print('Please type a number between 1 and 8 according to explaination given!!!')
        swallow()
def clubbing():
    global clubbing_
    clubbing_ = input('Clubbing of Finger Nails(1 for low, 8 for high)')
    clubbing_ = int(clubbing_)

    if not 1 <= clubbing_ <= 8:
        print('Please type a number between 1 and 8 according to explaination given!!!')
        clubbing()     
def cold():
    global cold_
    cold_ = input('Frequent Cold(1 for low, 8 for high)')
    cold_ = int(cold_)
    
    if not  1 <= cold_ <= 8:
        print('Please type a number between 1 and 8 according to explaination given!!!')
        cold()       
def dry():
    global dry_
    dry_ = input('Dry Coughing(1 for low, 8 for high)')
    dry_ = int(dry_)

    if not 1 <= dry_ <= 8:
        print('Please type a number between 1 and 8 according to explaination given!!!')
        dry()     
def snore():
    global snore_
    snore_ = input('Snoring(1 for low, 8 for high)')
    snore_ = int(snore_)
    
    if not 1 <= snore_ <= 8:
        print('Please type a number between 1 and 8 according to explaination given!!!')
        snore()

######################################################## DATA CONFIGURATION #####################################################################

data = pd.read_excel('cancer patient data sets.xlsx').replace(
    {
        'Low': 1,
        'Medium': 2,
        'High': 3 
    }
).dropna().drop(columns=['Patient Id'])

x = data.drop(columns=['Level'])
y = data['Level']

xtrain, xtest, ytrain, ytest = tts(x,y, train_size=0.2)

model = DecisionTreeClassifier()
model.fit(xtrain,ytrain)
prediction = model.predict(xtest)

score = scorer(ytest,prediction)
print(prediction)
###################################################### PLOT ############################################################################

a = list(range(0,prediction.size))
mt.scatter(a, prediction.ravel())
mt.scatter(a, ytest, color = 'r')
mt.show()

###################################################### USER INPUT ############################################################################
while True:
    age = input('Please type your age')
    gender()
    
    print('From now on please state the level of complaints asked (from 1 to 8)')
    pollution()
    alcohol()
    allergy()
    hazard()
    genetic()
    chronic()
    diet()
    obesity()
    smoking()
    passive()
    chest()
    cough()
    fatigue()
    weight()
    short()
    wheezing()
    swallow()
    clubbing()
    cold()
    dry()
    snore()

    user_input = np.array([[age, gender_, pollution_ , alcohol_, allergy_, hazard_, genetic_, chronic_, diet_, obesity_, smoking_, passive_, 
    
                            chest_, cough_, fatigue_, weight_, short_, wheezing_, swallow_, clubbing_,  cold_, dry_, snore_]])
    user_prediction = model.predict(user_input)
    print(user_prediction)