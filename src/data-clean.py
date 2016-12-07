import pandas as pd
import numpy as np
import pickle
#open adult.data or adult.test
data = pd.read_csv('../data/adult.test');
'''
Listing of attributes:
>50K, <=50K.
age: continuous.
workclass: Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.
fnlwgt: continuous.
education: Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool.
education-num: continuous.
marital-status: Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse.
occupation: Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces.
relationship: Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.
race: White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black.
sex: Female, Male.
capital-gain: continuous.
capital-loss: continuous.
hours-per-week: continuous.
native-country: United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands.
'''
#data clean
data = data.replace(' ?', np.nan)
#salary
# the format is different in adult.data and adult.test
# there is a full stop in adult.test
data = data.replace(' >50K.', 1)
data = data.replace(' <=50K.', 0)
#sex
data = data.replace(' Male', 1)
data = data.replace(' Female', 0)
#workclass
data = data.replace({' Private': 0, ' Self-emp-not-inc': 1 , ' Self-emp-inc':2 , ' Federal-gov': 3,\
' Local-gov':4 ,' State-gov': 5,  ' Without-pay': 6 , ' Never-worked':7})
#education
data = data.replace({' Bachelors':0, ' Some-college':1, ' 11th':2, ' HS-grad':3, ' Prof-school':4,\
 ' Assoc-acdm':5 , ' Assoc-voc':6, ' 9th':7, ' 7th-8th':8, ' 12th': 9, ' Masters':10, ' 1st-4th': 11,\
 ' 10th' : 12, ' Doctorate':13, ' 5th-6th':14, ' Preschool':15})
#marital-status
data = data.replace({' Married-civ-spouse':0, ' Divorced' :1, ' Never-married' :2, ' Separated': 3, ' Widowed' :4,\
 ' Married-spouse-absent':5, ' Married-AF-spouse':6})
#occupation
data = data.replace({' Tech-support':0, ' Craft-repair' :1, ' Other-service':2, ' Sales':3, ' Exec-managerial':4,\
 ' Prof-specialty':5, ' Handlers-cleaners':6, ' Machine-op-inspct':7, ' Adm-clerical':8, ' Farming-fishing':9,\
  ' Transport-moving':10, ' Priv-house-serv':11, ' Protective-serv':12, ' Armed-Forces':12})
#relationship
data = data.replace({ ' Wife':0, ' Own-child':1, ' Husband':2, ' Not-in-family':3, ' Other-relative':4, ' Unmarried':5})
#race
data = data.replace({' White':0, ' Asian-Pac-Islander':1, ' Amer-Indian-Eskimo':2, ' Other':3, ' Black':4})
#native-country
data = data.replace({ ' United-States':0, ' Cambodia':1, ' England':3, ' Puerto-Rico':4,' Canada':5,\
 ' Germany':6, ' Outlying-US(Guam-USVI-etc)':7, ' India':8, ' Japan':9, ' Greece':10, ' South':11,\
 ' China':12, ' Cuba':13, ' Iran':14, ' Honduras':15, ' Philippines':16, ' Italy':17, ' Poland':18,\
 ' Jamaica':19, ' Vietnam':20, ' Mexico':21, ' Portugal':22, ' Ireland':23, ' France':24, ' Dominican-Republic':25,\
 ' Laos':26, ' Ecuador':27, ' Taiwan':27, ' Haiti':28, ' Columbia':29, ' Hungary':30, ' Guatemala':31, ' Nicaragua':32,\
 ' Scotland':33, ' Thailand':34, ' Yugoslavia':35, ' El-Salvador':36, ' Trinadad&Tobago':37, ' Peru':38,
 ' Hong':39, ' Holand-Netherlands':40})

#drop the NAN values
data = data.dropna()
#print data
data_X = data.ix[:,:'native-country']
data_X = np.array(data_X)
#print data_X
pickle.dump(data_X, open('data_X_test.txt','w'))
data_Y = data['salary']
data_Y = np.array(data_Y)
pickle.dump(data_Y,open('data_Y_test.txt','w'))
#print data_Y
