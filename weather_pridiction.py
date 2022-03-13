import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
df=pd.read_csv('C:/Users/Yash Kumar Soni/OneDrive/Pictures/Video Projects/new_dataset.csv') #read csv file
print(df)

#encoder the string to Numerics
Numerics=LabelEncoder()
#dropping the target variable and make it as a new frame 
inputs=df.drop('Play',axis='columns')
target =df['Play']
print(target)

#creating a new data frame
inputs['Outlooks_n']=Numerics.fit_transform(inputs['Outlook'])
inputs['Temp_n']=Numerics.fit_transform(inputs['Temp'])
inputs['Humidity_n']=Numerics.fit_transform(inputs['Humidity'])
inputs['Windy_n']=Numerics.fit_transform(inputs['Windy'])

inputs_n=inputs.drop(['Outlook','Temp','Humidity','Windy'], axis='columns')
print(inputs_n)


#apply the gaussian naivebyes
Classifier=GaussianNB()
Classifier.fit(inputs_n, target)


#prediction
#outlook=rainy ,Temp='hot', humidity='high',  windy='False

#here array value is NO that means it is not a suitable 
# condition to play a match
print(Classifier.predict([[1,0,0,0]]))
