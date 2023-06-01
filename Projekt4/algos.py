import pandas as pd
pd.set_option('display.max_columns', None)
df=pd.read_csv("heart.csv",sep=',')
df.head()

y=df['target']
df.drop('target',axis=1,inplace=True)
numberOfAtributtes= len(df.columns)

from main_features_DecisionTreeClassifier import DTCParametersFeatureFitness
from main_features_KNeighborsClassifier import KNCParametersFeatureFitness
from main_features_LogisticRegression import LRCParametersFeatureFitness
from main_features_RandomForestClassifier import RFCParametersFeatureFitness
from main_features_GradientBoostingClassifier import GBCParametersFeatureFitness

ind_kn =  [2, 'uniform', 'ball_tree', 20, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0]
ind_lr = [0.1579853859402021, 'saga', 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0]
ind_rforest = [2, 'gini', 13, 'sqrt', 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1]
ind_grad = [0.004180218226607635, 'exponential', 25, 2, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1]
ind_decision_tree = ['entropy', 'random', 'sqrt', 2, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1]

print(f'{numberOfAtributtes=}')

print(f'{DTCParametersFeatureFitness(y,df,numberOfAtributtes,ind_decision_tree)=}')  
print(f'{KNCParametersFeatureFitness(y,df,numberOfAtributtes,ind_kn)=}')  
print(f'{LRCParametersFeatureFitness(y,df,numberOfAtributtes,ind_lr)=}')  
print(f'{RFCParametersFeatureFitness(y,df,numberOfAtributtes,ind_rforest)=}')  
print(f'{GBCParametersFeatureFitness(y,df,numberOfAtributtes,ind_grad)=}')  

