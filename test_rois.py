import collections
import pandas as pd 
from sovaViolin.functions_rois import compare_norm_1D_1G_nB_nV_1ROI_power



F = ['FP1', 'FPZ', 'FP2', 'AF3', 'AF4', 'F7', 'F5', 'F3', 'F1', 'FZ', 'F2', 'F4', 'F6', 'F8'] 
T = ['FT7', 'FC5', 'FC6', 'FT8', 'T7', 'C5', 'C6', 'T8', 'TP7', 'CP5', 'CP6', 'TP8']
C = ['FC3', 'FC1', 'FCZ', 'FC2', 'FC4', 'C3', 'C1', 'CZ', 'C2', 'C4', 'CP3', 'CP1', 'CPZ', 'CP2', 'CP4'] 
PO = ['P7', 'P5', 'P3', 'P1', 'PZ', 'P2', 'P4', 'P6', 'P8', 'PO7', 'PO5', 'PO3', 'POZ', 'PO4', 'PO6', 'PO8', 'CB1', 'O1', 'OZ', 'O2', 'CB2']
rois = [F,C,PO,T]
roi_labels = ['F','C','PO','T']


datos1=pd.read_excel(r"Dataframes\longitudinal_data_powers_long_channels_norm.xlsx") 
datos2=pd.read_excel(r"Dataframes\longitudinal_data_powers_long_channels.xlsx")
datos=pd.concat((datos1,datos2))
for i in range(len(rois)):
    filas=datos.Channels.isin(rois[i])
    datos.loc[filas,'Roi']=roi_labels[i]

datos=datos.drop(datos[datos['Session']=='V4P'].index)#Borrar datos

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
    datos['Group']=datos['Group'].replace({'CTR':'Control','G2':'Control'})
    return datos


datos=pair_data(datos)
ROIS=datos['Roi'].unique()
for roi in ROIS:
    compare_norm_1D_1G_nB_nV_1ROI_power(datos,'BIOMARCADORES',roi,num_col=4, save=False,plot=True)