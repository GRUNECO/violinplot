from numpy import True_
from datasets import BIOMARCADORES
from sovaViolin.functions_postprocessing_components import compare_norm_1D_1G_nB_ncomp_power,compare_norm_1D_1G_1B_nV_ncomp_power,compare_norm_1D_1G_1B_nV_all_comp_power
import pandas as pd 

# datos1=pd.read_excel(r"Dataframes\longitudinal_data_powers_long_components.xlsx") 
# datos2=pd.read_excel(r"Dataframes\longitudinal_data_powers_long_components_norm.xlsx")
# datos=pd.concat((datos1,datos2))
datos1=pd.read_feather(r'F:\BIOMARCADORES\derivatives\longitudinal_data_powers_long_CE_components.feather')
datos2=pd.read_feather(r'F:\BIOMARCADORES\derivatives\longitudinal_data_powers_long_CE_norm_components.feather')
datos=pd.concat((datos1,datos2))

GB = ['G1','CTR','DCL','DTA']
## Graphics for groups in components 
# for gr in GB:
#     compare_norm_1D_1G_nB_ncomp_power(datos,'BIOMARCADORES',gr,save=False)


## Graphics for groups and all visits in components 
def pair_data(datos):
    datos=datos.drop(datos[datos['Session']=='V4P'].index)#Borrar datos
    datos['Session']=datos['Session'].replace({'VO':'V0','V4P':'V4'})
    groups=['CTR','G2'] # Pair groups 
    datos=datos[datos.Group.isin(groups) ] #Only data of CTR y G2
    visitas=['V0','V1','V2','V3']
    #Script for drop subjects without four sessions select
    for i in groups:
        g=datos[datos['Group']==i]
        sujetos=g['Subject'].unique()
        print('Cantidad de sujetos de '+i+': ', len(sujetos))
        k=0
        for j in sujetos:
            s=g[g['Subject']==j]
            if len(s['Session'].unique()) !=4:
                k=k+1
                datos=datos.drop(datos[datos['Subject']==j].index)
            if len(s['Session'].unique()) ==4:
                v=s['Session'].unique()
                for vis in range(len(visitas)):
                    datos.loc[(datos.Subject==j)&(datos.Session==v[vis]),'Session']=visitas[vis]
                    #datos[datos['Subject']==j]['Session'].replace({v[vis]:visitas[vis]})        
        print('Sujetos a borrar:', k)
        print('Sujetos a analizar con 4 visitas: ',len(sujetos)-k)
    for i in groups:
        g=datos[datos['Group']==i]
        print('Cantidad de sujetos al filtrar '+ i+': ',len(g['Subject'].unique()))
    visitas=['V0','V1','V2','V3']
    datos['Group']=datos['Group'].replace({'CTR':'CTR','G2':'CTR'})
    return datos

datos=pair_data(datos)
bands= datos['Bands'].unique()
for band in bands:
    compare_norm_1D_1G_1B_nV_ncomp_power(datos,'BIOMARCADORES','CTR',band,num_columns=4, save=False,plot=True,encode=False)
    
