import pandas as pd
pd.set_option('display.max_columns', None)
df=pd.read_csv("./ReplicatedAcousticFeatures.csv",sep=',')
y=df['Status']
df.drop('Status',axis=1,inplace=True)
df.drop('ID',axis=1,inplace=True)
df.drop('Recording',axis=1,inplace=True) 

numberOfAtributtes= len(df.columns)

from main_features_DecisionTreeClassifier import DTCParametersFeatureFitness
from main_features_KNeighborsClassifier import KNCParametersFeatureFitness
from main_features_LogisticRegression import LRCParametersFeatureFitness
from main_features_RandomForestClassifier import RFCParametersFeatureFitness
from main_features_GradientBoostingClassifier import GBCParametersFeatureFitness

ind_decision_tree = ['entropy', 'best', 'sqrt', 93, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0]
ind_grad = [0.874829110382808, 'deviance', 73, 2, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0]
ind_kn =  [2, 'distance', 'ball_tree', 84, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1]
ind_lr = [0.5800893666343226, 'liblinear', 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1]
ind_rforest = [12, 'gini', 9, 'log2', 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1]

print(f'{numberOfAtributtes=}')

print(f'{DTCParametersFeatureFitness(y,df,numberOfAtributtes,ind_decision_tree)=}')  
print(f'{KNCParametersFeatureFitness(y,df,numberOfAtributtes,ind_kn)=}')  
print(f'{LRCParametersFeatureFitness(y,df,numberOfAtributtes,ind_lr)=}')  
print(f'{RFCParametersFeatureFitness(y,df,numberOfAtributtes,ind_rforest)=}')  
print(f'{GBCParametersFeatureFitness(y,df,numberOfAtributtes,ind_grad)=}')  

