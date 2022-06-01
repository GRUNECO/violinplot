from numpy import True_
from datasets import BIOMARCADORES
#from Graphics.GetDataframes import get_dataframe_powers_components
from sovaViolin.functions_postprocessing_components import compare_norm_1D_1G_nB_ncomp_power,compare_norm_1D_1G_1B_nV_ncomp_power,compare_norm_1D_1G_1B_nV_all_comp_power
import pandas as pd 
import os 
import collections

datos1=pd.read_excel(r"Dataframes\longitudinal_data_powers_long_components_norm.xlsx") 
datos2=pd.read_excel(r"Dataframes\longitudinal_data_powers_long_components.xlsx")
datos=pd.concat((datos1,datos2))

datos=datos.drop(datos[datos['Session']=='V4P'].index)#Borrar datos
sessions=datos['Session'].unique() #sesiones 

G=['G1','G2']

for i in G:
    g=datos[datos['Group']==i]
    visitas=g['Session'].unique()
    sujetos=g['Subject'].unique()
    print('Cantidad de sujetos de '+i+': ', len(sujetos))
    k=0
    for j in sujetos:
        s=g[g['Subject']==j]
        if (collections.Counter(s['Session'].unique()) == collections.Counter(visitas)):
            None
        else:
            k=k+1
            datos=datos.drop(datos[datos['Subject']==j].index)
            #print(j) #Sujeto sin todas 
            #print(s['Session'].unique())
    print('Sujetos a borrar:', k)
    print('Sujetos a analizar con todas las visitas: ',len(sujetos)-k)

datos=datos[datos.Group.isin(G)]

#GB = ['G1','CTR','DCL','DTA']
## Graphics for groups in components 
# for gr in GB:
#     compare_norm_1D_1G_nB_ncomp_power(datos,'BIOMARCADORES',gr,save=False)


## Graphics for groups and all visits in components 
bands= datos['Bands'].unique()

for gr in G:
    for band in bands:
        compare_norm_1D_1G_1B_nV_ncomp_power(datos,'BIOMARCADORES',gr, band,num_columns=4, save=True,plot=True,encode=False)
        