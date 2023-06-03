import pandas as pd
pd.set_option('display.max_columns', None)
df=pd.read_csv("heart.csv",sep=',')
df.head()

y=df['target']
df.drop('target',axis=1,inplace=True)
numberOfAtributtes= len(df.columns)

from main_features_DecisionTreeClassifier import DTCParametersFeatureFitness, DTCParametersFitness, DTCDefault
from main_features_KNeighborsClassifier import KNCParametersFeatureFitness, KNCParametersFitness, KNCDefault
from main_features_LogisticRegression import LRCParametersFeatureFitness, LRCParametersFitness, LRCDefault
from main_features_RandomForestClassifier import RFCParametersFeatureFitness, RFCParametersFitness, RFCDefault
from main_features_GradientBoostingClassifier import GBCParametersFeatureFitness, GBCParametersFitness, GBCDefault

ind_kn =   [2, 'uniform', 'ball_tree', 20, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0]
ind_lr =  [0.1579853859402021, 'saga', 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0]
ind_rforest = [12, 'entropy', 10, 'log2', 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1]
ind_grad = [0.8296793479046654, 'log_loss', 30, 2, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1]
ind_decision_tree = ['log_loss', 'random', 'log2', 5, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1]

print(f'{numberOfAtributtes=}')

print(f'{DTCParametersFeatureFitness(y,df,numberOfAtributtes,ind_decision_tree)=}')  
print(f'{KNCParametersFeatureFitness(y,df,numberOfAtributtes,ind_kn)=}')  
print(f'{LRCParametersFeatureFitness(y,df,numberOfAtributtes,ind_lr)=}')  
print(f'{RFCParametersFeatureFitness(y,df,numberOfAtributtes,ind_rforest)=}')  
print(f'{GBCParametersFeatureFitness(y,df,numberOfAtributtes,ind_grad)=}')  

ind_no_ft__decision_tree = ['log_loss', 'random', 'log2', 2]
ind_no_ft__grad = [0.16213212059446314, 'exponential', 29, 6]
ind_no_ft__kn =  [1, 'distance', 'brute', 40]
ind_no_ft__lr = [0.8306848874726929, 'liblinear']
ind_no_ft_rforest = [2, 'entropy', 8, 'sqrt']

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