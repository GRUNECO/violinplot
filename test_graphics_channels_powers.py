from datasets import BIOMARCADORES
from Graphics.GetDataframes import get_dataframe_powers
from Graphics.functions_postprocessing_channels import compare_1D_nB_0C_power, compare_1D_1V_nB_power,compare_1D_1G_nB_0C_power,compare_1D_nV_nB_power,compare_1D_1B_nC_power, compare_nD_nB_power,compare_nD_nG_nB_power,compare_nD_power,compare_norm_1D_1G_nB_power,compare_norm_1D_1G_nB_nV_power
import pandas as pd
import seaborn as sns
import numpy as np

''' 
# Just run one time for save the csv and concat the normalize and preprocessing data

Studies=[BIOMARCADORES]
datos=get_dataframe_powers(Studies,mode="norm") # normalized dataframe 
datos1=get_dataframe_powers(Studies,mode=None) # whitout normalized dataframe 
data=pd.concat((datos,datos1)) # concatenate dataframes 
data.to_csv('dataframe.csv',index=False) # saved dataframe
''' 
datos=pd.read_csv(r'Dataframes\dataframe_norm_biomarcadores.csv',sep=",")

datos['Session']=datos['Session'].replace({'VO':'V0'})
datos['Group']=datos['Group'].replace({'G2':'CTR'})


#********************* WHITOUT NORMALIZING *****************************************


# # TOTAL
# compare_nD_power(datos,plot=True)

# #n estudios 
# compare_nD_nB_power(datos,name_channel="None")

# #n grupos 
# info={
#    'SRM':['SRM'],
#    'BIOMARCADORES':['G1','G2','CTR','DCL','DTA']
#    #'CHBMP':['CHBMP']
# }
# compare_nD_nG_nB_power(datos,info)
# # n sessions
# #compare_1D_nV_nB_power(datos,'BIOMARCADORES')
# compare_1D_nV_nB_power(datos,'SRM')


#********************* NORMALIZING *****************************************

GB = ['G1','CTR','DCL','DTA']
#Graficos por grupo de todas las bandas comparando potencias normalizadas y no normalizadas

# for gr in GB:
#     compare_norm_1D_1G_nB_power(datos,'BIOMARCADORES',gr,save=True)
for gr in GB:
    compare_norm_1D_1G_nB_nV_power(datos,'BIOMARCADORES',gr,save=False)

''' NO SE NECESITA AÚN
# 1 estudio
St=['CHBMP','BIOMARCADORES','SRM']
St=['BIOMARCADORES','SRM']
bands_1 = ['delta','theta','alpha-1','alpha-2','beta-1','beta-3','gamma']
GB = ['G1','G2','CTR','DCL','DTA']
Vs = ['V0','V1','V2','V3','V4']

for Study in St:
    compare_1D_nB_0C_power(datos,Study,plot=True)
    compare_1D_nV_nB(datos,Study)
    for gr in GB:
        compare_1D_1G_nB_0C_power(datos,Study,gr,plot=True)
    for V in Vs:
        compare_1D_1V_nB(datos,Study,V,True)        
    for band in bands_1:
        compare_1D_1B_nC_power(datos,Study,band,plot=True)
St=['BIOMARCADORES','SRM']
bands_1 = ['delta','theta','alpha-1','alpha-2','alpha','beta','gamma']
GB = ['G1','G2','CTR','DCL','DTA']

for Study in St:
    compare_1D_nB_0C_power(datos,Study,plot=True)
    # NOTA: Este gráfico por el momento no es representativo           
    # for band in bands_1:
    #     compare_1D_1B_nC_power(datosPowers,Study,band,plot=True)

#n estudios
# NOTA: Esta función por el momento no es representativa
channels = ['FP1', 'FPZ', 'FP2', 'AF3']
#, 'AF4', 'F7', 'F5', 'F3', 'F1', 'FZ', 'F2', 'F4', 'F6', 'F8', 'FC5', 'FC3', 'FC1', 'FCZ', 'FC2', 'FC4', 'FC6', 'T7', 'C5', 'C3', 'C1', 'CZ', 'C2', 'C4', 'C6', 'T8', 'TP7', 'CP5', 'CP3', 'CP1', 'CPZ', 'CP2', 'CP4', 'CP6', 'TP8', 'P7', 'P5', 'P3', 'P1', 'PZ', 'P2', 'P4', 'P6', 'P8', 'PO7', 'PO5', 'PO3', 'POZ', 'PO4', 'PO6', 'PO8', 'O1', 'OZ', 'O2']
for channel in channels:
    compare_nD_nB_power(datosPowers,name_channel=channel)



#Nota: Solo es útil para cuando el usuario quiera un grupo en especifico, de lo contrario
esta la función para n grupos

GB= ['G1','G2','CTR','DCL','DTA']
# 1  grupo
for G in GB:
    compare_1S_1G_nB_0C_power(datosPowers,'BIOMARCADORES',G,plot=True)



# 1 sessions
# Solo es útil si se quiere una gráfica en especifico , para ver todas es mejor usar para nV
Vs = ['V0','V1','V2','V3','V4']
Vs_SRM=['t1','t2']
for V in Vs:
    compare_1D_1V_nB(datosPowers,'BIOMARCADORES',V,True)
for V in Vs_SRM:
    compare_1D_1V_nB(datosPowers,'SRM',V,True)


'''

