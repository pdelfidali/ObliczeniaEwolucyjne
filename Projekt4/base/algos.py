import pandas as pd
pd.set_option('display.max_columns', None)
df=pd.read_csv("./ReplicatedAcousticFeatures.csv",sep=',')
y=df['Status']
df.drop('Status',axis=1,inplace=True)
df.drop('ID',axis=1,inplace=True)
df.drop('Recording',axis=1,inplace=True) 

numberOfAtributtes= len(df.columns)

from main_features_DecisionTreeClassifier import DTCParametersFeatureFitness, DTCParametersFitness, DTCDefault
from main_features_KNeighborsClassifier import KNCParametersFeatureFitness, KNCParametersFitness, KNCDefault
from main_features_LogisticRegression import LRCParametersFeatureFitness, LRCParametersFitness, LRCDefault
from main_features_RandomForestClassifier import RFCParametersFeatureFitness, RFCParametersFitness, RFCDefault
from main_features_GradientBoostingClassifier import GBCParametersFeatureFitness, GBCParametersFitness, GBCDefault

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


ind_no_ft__decision_tree = ['gini', 'random', 'sqrt', 65]
ind_no_ft__grad = [0.002558704058075678, 'exponential', 23, 5]
ind_no_ft__kn =  [2, 'distance', 'kd_tree', 94]
ind_no_ft__lr = [0.8103097098006129, 'liblinear']
ind_no_ft_rforest = [20, 'gini', 30, 'log2']

print(f'{DTCParametersFitness(y,df,numberOfAtributtes,ind_no_ft__decision_tree)=}')  
print(f'{KNCParametersFitness(y,df,numberOfAtributtes,ind_no_ft__kn)=}')  
print(f'{LRCParametersFitness(y,df,numberOfAtributtes,ind_no_ft__lr)=}')  
print(f'{RFCParametersFitness(y,df,numberOfAtributtes,ind_no_ft_rforest)=}')  
print(f'{GBCParametersFitness(y,df,numberOfAtributtes,ind_no_ft__grad)=}') 


print('================================DEFAULTS =================================================')
print(f'{DTCDefault(y,df)=}')  
print(f'{KNCDefault(y,df)=}')  
print(f'{LRCDefault(y,df)=}')  
print(f'{RFCDefault(y,df)=}')  
print(f'{GBCDefault(y,df)=}') 

