from numpy import True_
from datasets import BIOMARCADORES
#from Graphics.GetDataframes import get_dataframe_powers_components
from sovaViolin.functions_postprocessing_components import compare_norm_1D_1G_nB_ncomp_power,compare_norm_1D_1G_1B_nV_ncomp_power,compare_norm_1D_1G_1B_nV_all_comp_power
import pandas as pd 
import os 

datos1=pd.read_excel(r"Dataframes\longitudinal_data_powers_long_components.xlsx") 
datos2=pd.read_excel(r"Dataframes\longitudinal_data_powers_long_components_norm.xlsx")
datos=pd.concat((datos1,datos2))

GB = ['G1','CTR','DCL','DTA']
## Graphics for groups in components 
# for gr in GB:
#     compare_norm_1D_1G_nB_ncomp_power(datos,'BIOMARCADORES',gr,save=False)


## Graphics for groups and all visits in components 
bands= datos['Bands'].unique()
# for gr in GB:
print(datos['Group'].unique())
datos['Group']=datos['Group'].replace({'G2':'CTR'})
print(datos['Group'].unique())

bands=datos['Bands'].unique()
for band in bands:
    compare_norm_1D_1G_1B_nV_ncomp_power(datos,'BIOMARCADORES','CTR',band,num_columns=4, save=False,plot=True,encode=False)
    
