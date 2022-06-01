from tokenize import group
import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
#from .functionsImages import create_collage,createCollage,fig2img_encode
import numpy as np
import pandas as pd 
import collections

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

def compare_norm_1D_1G_1B_nV_ncomp_power(data,name_dataset,name_band, save=False,plot=False):
    '''
    Componentes de interés
    C14, C15, C18, C20, C22, C23, C24, C25 

    Parameters
    ----------
        data: dataframe
        name_dataset: str
        name_group: str
        name_band: str 
        save: Boolean 
        plot: Boolean 
        encode: Boolean

    Returns 
    ----------
        img_encode
    '''
    #data['Session']=data['Session'].replace({'VO':'V0'})
    #data['Group']=data['Group'].replace({'G2':'CTR'})
    filter=data["Study"]==name_dataset
    filter_group_dataset=data[filter]
    sns.set(rc={'figure.figsize':(11.7,8.27)})
    sns.set_theme(style="white")
    axs=sns.catplot(x='Session',y="Powers",data=filter_group_dataset,hue='Stage',dodge=True, kind="box",col='Roi',row='Group',palette='winter_r',fliersize=1.5,linewidth=0.5,legend=False)
    #plt.yticks(np.arange(0,1,0.1))
    axs.set(xlabel=None)
    axs.set(ylabel=None)
    axs.fig.suptitle('Relative '+ name_band+ ' power of normalized and preprocessed data in ROI and all visits')
    axs.add_legend(loc='upper center',bbox_to_anchor=(.5,.96),ncol=2)
    axs.fig.subplots_adjust(top=0.857,bottom=0.121, right=0.986,left=0.05, hspace=0.138, wspace=0.062) # adjust the Figure in rp
    axs.fig.text(0.5, 0.04, 'Visits', ha='center', va='center')
    axs.fig.text(0.01, 0.5,  'Relative powers', ha='center', va='center',rotation='vertical')
    if save==True:
        plt.savefig('Resultados\Graphics_rois\{name_dataset}_{name_band}_rois.png'.format(name_dataset=name_dataset,name_band=name_band))
        plt.close()
    if plot:
        plt.show()
    return 

bandas=datos['Bands'].unique()

for band in bandas:
    d_band=datos[datos['Bands']==band]
    compare_norm_1D_1G_1B_nV_ncomp_power(d_band,'BIOMARCADORES',band, save=True,plot=False)
    
