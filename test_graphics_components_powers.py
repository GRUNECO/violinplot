from numpy import True_
from datasets import BIOMARCADORES
#from Graphics.GetDataframes import get_dataframe_powers_components
from sovaViolin.functions_postprocessing_components import compare_norm_1D_1G_nB_ncomp_power,compare_norm_1D_1G_1B_nV_ncomp_power,compare_norm_1D_1G_1B_nV_all_comp_power
import pandas as pd 
import os 

''' 
# Just run one time for save the csv and concat the normalize and preprocessing data

get_dataframe_powers_components([BIOMARCADORES], stage=None)
get_dataframe_powers_components([BIOMARCADORES], stage="norm")
icpowers_long=pd.read_excel(r'Dataframes\longitudinal_data_icpowers_long.xlsx')
icpowers_norm_long=pd.read_excel(r'Dataframes\longitudinal_data_icpowers_norm_long.xlsx')
data=pd.concat((icpowers_long,icpowers_norm_long)) # concatenate dataframes 
data.to_csv('Dataframes\longitudinal_data_icpowers_long_norm.csv',index=False) # saved dataframe

'''

def load_feather(path):
    data=pd.read_feather(os.path.join(path).replace("\\","/"))
    return data

data_comp=r'F:\BIOMARCADORES\derivatives\longitudinal_data_powers_long_components.feather'
data_comp_norm=r'F:\BIOMARCADORES\derivatives\longitudinal_data_powers_long_components_norm.feather'

data=load_feather(data_comp)
data_norm=load_feather(data_comp_norm)

datos=pd.concat((data,data_norm))

GB = ['G1','CTR','DCL','DTA']
## Graphics for groups in components 
# for gr in GB:
#     compare_norm_1D_1G_nB_ncomp_power(datos,'BIOMARCADORES',gr,save=False)


## Graphics for groups and all visits in components 
bands= datos['Bands'].unique()
for gr in GB:
    compare_norm_1D_1G_1B_nV_all_comp_power(datos,'BIOMARCADORES',gr,num_columns=4, save=True,plot=Falsee,encode=False)
