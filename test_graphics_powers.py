from tokenize import group
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
from datasets import CHBMP, LEMON,BIOMARCADORES,SRM
from Graphics.graphicsViolin import get_dataframe_powers
import numpy as np
import itertools
from pprint import pprint

# CHBMP, LEMON
from matplotlib.gridspec import GridSpec

Studies=[BIOMARCADORES,SRM]
#Studies_test=[BIOMARCADORES_test,SRM_test]

datosPowers=get_dataframe_powers(Studies)

# POTENCIAS ENTRE ESTUDIOS 

def compare_1S_nB_0C_power(data,name_study,plot=False):
    """
    todos sujetos -1 estudio- 1 grupo -todas las bandas sin distinguir el canal
    """ 
    data=data.drop(["Channels"],axis=1,inplace=False)
    s=data["Study"]==name_study
    filter_study=data[s]
    bandas=filter_study["Bands"].unique()

    fig, ax = plt.subplots(1,1)
    fig.set_size_inches(len(bandas)*2,10)
    sns.violinplot(x='Bands',y="Powers",data=filter_study)
    ax.set_title('Bands powers for the '+name_study)
    if plot:
        plt.show()
    return fig 

def compare_1S_1B_nC_power(data,name_study,name_band,plot=False):
    """
    todos sujetos, 1 estudio 1 grupo 1 banda por canal
    
    """
    b=np.logical_and(data["Bands"]==name_band, data["Study"]==name_study)
    filter_band=data[b]
    channels=data["Channels"].unique()
    # f=8
    # c=8
    # fig,axs= plt.subplots(f,c,figsize=(c*3,f*3)) 
    # axs=list(itertools.chain(*axs))
    # print(axs)
    # for i,nombreColumna in enumerate(channels):
    #   sns.violinplot(data=filter_band[filter_band['Channels']==nombreColumna],ax=axs[i]) 
    #   axs[i].set_title(nombreColumna)
    
    fig, ax = plt.subplots(1,1)
    fig.set_size_inches(len(channels)*2,10)
    sns.violinplot(x='Channels',y="Powers",data=filter_band)
    ax.set_title('Bands powers for the '+name_study+'-'+name_band)
    fig.tight_layout()
    if plot:
        plt.show()
    return fig 

def filter_nS_1B_1C_power(data,name_band,channel):
    "todos sujetos, n estudios 1 bandas por 1 canal"
    fil_B_C=np.logical_and(data["Bands"]==name_band,data["Channels"]==channel)
    filter=data[fil_B_C]
    return filter

def filter_nS_nB_0C_power(data,name_band):
    fil_B=data["Bands"]==name_band
    filter=data[fil_B]
    return filter 

def compare_nS_nB_power(data,name_channel="None",plot=False):
    bandas=data["Bands"].unique()
    rows=1
    cols=7
    fig,axs=plt.subplots(rows,cols,figsize=(12,3))
    #en un canal especifico
    if name_channel != "None":
        for col,band in zip(range(cols),bandas):
            filter= filter_nS_1B_1C_power(data,band,name_channel) 
            sns.violinplot(x='Study',y="Powers",data=filter,ax=axs[col],scale_hue=True,scale='width')
            axs[col].set_title(band+' '+name_channel)
        plt.tight_layout(pad=0.4, w_pad=0.0001, h_pad=0.8)
        if plot:
            plt.show()
    
    else: 
        #sin distinguir el canal
        for col,band in zip(range(cols),bandas):
            filter= filter_nS_nB_0C_power(data,band)
            sns.violinplot(x='Study',y="Powers",data=filter,ax=axs[col])
            axs[col].set_title(band)
        plt.tight_layout(pad=0.4, w_pad=0.0001, h_pad=0.8)
        if plot:
            plt.show()
    return 
    

#POTENCIAS POR GRUPO 

def compare_1S_1G_nB_0C_power(data,name_study,name_group,plot=False):
    """
    todos sujetos -1 estudio- 1 grupo -todas las bandas sin distinguir el canal
    """ 
    data=data.drop(["Channels"],axis=1,inplace=False)
    s=np.logical_and(data["Study"]==name_study,data["Group"]==name_group)
    filter=data[s]
    #filter_group=filter_study[filter_study.Subject.str.contains(name_group)]
    bandas=filter["Bands"].unique()

    fig, ax = plt.subplots(1,1)
    fig.set_size_inches(len(bandas)*2,10)
    sns.violinplot(x='Bands',y="Powers",data=filter)
    if plot:
        plt.show()
    return fig 

def filter_1S_1G_1B(data,name_study,name_band,name_group):
    fil=np.logical_and(data["Bands"]==name_band, data["Study"]==name_study,data["Group"]==name_group)
    filter=data[fil]
    return filter 

def compare_nS_1G_nB(data,dict_info,plot=False):
    fig,axs=plt.subplots(len(dict_info.keys()),7,sharex=True)
    #fig=plt.figure(figsize=(30,60), dpi=30)
    bands=data['Bands'].unique()
    for j,band in enumerate(bands):     
        for i,key in enumerate(dict_info):
            if dict_info[key]==list: 
                for value in dict_info[key]:
                    filter_group=filter_1S_1G_1B(data,key,band,value)
                    sns.violinplot(x='Study',y="Powers",data=filter_group,ax=axs[i,j])
                    axs[i,j].set_title(band)
            else:
                filter_group=filter_1S_1G_1B(data,key,band,dict_info[key])
                sns.violinplot(x='Study',y="Powers",data=filter_group,ax=axs[i,j])
                if dict_info[key]=='':
                  axs[i,j].set_title(band +' CTR')      
                axs[i,j].set_title(band +dict_info[key])            
    plt.tight_layout()     
    if plot:
        plt.show()
    return fig 

#POTENCIAS POR VISITA 

def compare_1S_1V_nB(data,name_study,name_session,plot=False):
    data=data.drop(["Channels"],axis=1,inplace=False)
    b=np.logical_and(data["Study"]==name_study,data["Session"]==name_session)
    filter=data[b]
    bandas=filter["Bands"].unique()

    fig, ax = plt.subplots(1,1)
    fig.set_size_inches(len(bandas)*2,10)
    sns.violinplot(x='Bands',y="Powers",data=filter)
    ax.set_title("Bandas de frecuencia en: "+name_study+'-'+name_session)
    if plot:
        plt.show()
    return fig 

def filter_1S_1V_1B(data,name_study,name_band):
    b=np.logical_and(data["Bands"]==name_band, data["Study"]==name_study)
    filter=data[b]
    return filter

def compare_1S_nV_nB(data,name_study,plot=False): 
    sessions=data['Session'].unique()
    rows=3
    cols=3
    fig,axs=plt.subplots(rows,cols,figsize=(6,12))
    #fig = plt.figure(figsize=(6, 6))
    #grid = plt.GridSpec(4, 4, hspace=0.2, wspace=0.2)
    bands=data['Bands'].unique()
    rows=np.arange(rows).repeat(3)
    columnas=np.concatenate((np.array([np.arange(3)]*3)))
    for row,col,band in zip(rows,columnas,bands):
    #for num,band in enumerate(band):
        filter_group=filter_1S_1V_1B(data,name_study,band)
        sns.violinplot(x='Session',y="Powers",data=filter_group,ax=axs[row,col])
        #axs[row,col].set_title(band)
    plt.tight_layout()     
    if plot:
        plt.show()
    return fig  


#def compare_nS_1V_nB(data,dict_info,plot=False)

info={
    'BIOMARCADORES':['V1','V2','V3','V4'],
}
compare_1S_nV_nB(datosPowers,'BIOMARCADORES',True)

'''

# 1 estudio
compare_1S_nB_0C_power(datosPowers,'SRM',plot=True)
compare_1S_1B_nC_power(datosPowers,'SRM','delta',plot=True)
# n estudios 
create_collage(3,3,1200, 1000, compare_nS_7B_power(datosPowers,'FPZ'),'FPZ')
create_collage(3,3,1200, 1000, compare_nS_7B_power(datosPowers))
para evitar guardar imágenes usar estas funciones

#NOTA: ORGANIZAR PARA QUE SALGAN POR ROWS Y COLS
compare_nS_nB_power(datosPowers,name_channel='FPZ',plot=True)
compare_nS_nB_power(datosPowers,name_channel="None",plot=True)

# 1  grupo

'''
# n grupos
info={
    'BIOMARCADORES':'CTR',
    'SRM':''
}
compare_nS_1G_nB(datosPowers,info,True)

'''
# sessions
compare_1S_1V_nB(datosPowers,'SRM','t1',plot=True)
'''

