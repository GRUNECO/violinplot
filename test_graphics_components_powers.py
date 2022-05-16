from datasets import BIOMARCADORES
#from Graphics.GetDataframes import get_dataframe_powers_components
from sovaViolin.functions_postprocessing_components import compare_norm_1D_1G_nB_ncomp_power,compare_norm_1D_1G_1B_nV_ncomp_power
import pandas as pd 

''' 
# Just run one time for save the csv and concat the normalize and preprocessing data

get_dataframe_powers_components([BIOMARCADORES], stage=None)
get_dataframe_powers_components([BIOMARCADORES], stage="norm")
icpowers_long=pd.read_excel(r'Dataframes\longitudinal_data_icpowers_long.xlsx')
icpowers_norm_long=pd.read_excel(r'Dataframes\longitudinal_data_icpowers_norm_long.xlsx')
data=pd.concat((icpowers_long,icpowers_norm_long)) # concatenate dataframes 
data.to_csv('Dataframes\longitudinal_data_icpowers_long_norm.csv',index=False) # saved dataframe

'''

datos=pd.read_excel(r'Dataframes\longitudinal_data_powers_long_components_norm.xlsx')
GB = ['G1','CTR','DCL','DTA']
## Graphics for groups in components 
# for gr in GB:
#     compare_norm_1D_1G_nB_ncomp_power(datos,'BIOMARCADORES',gr,save=False)

## Graphics for groups and all visits in components 
bands= datos['Bands'].unique()
for gr in GB:
    for band in bands:
        compare_norm_1D_1G_1B_nV_ncomp_power(datos,'BIOMARCADORES',gr,band,save=False)