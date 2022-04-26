from tokenize import group
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
from datasets import CHBMP, LEMON,BIOMARCADORES,SRM,BIOMARCADORES_test,SRM_test
from Graphics.FunctionsGraphics import create_collage,createCollage
from Graphics.GetDataframes import get_dataframe_powers
import numpy as np
import itertools
from pprint import pprint

# CHBMP, LEMON
from matplotlib.gridspec import GridSpec

Studies=[CHBMP,BIOMARCADORES,SRM]
#Studies=[LEMON]
#Studies_test=[BIOMARCADORES_test,SRM_test]

datosPowers=get_dataframe_powers(Studies)

# TOTAL
def compare_nD(data,plot=False):
    """
    todos sujetos -1 estudio- 1 grupo -todas las bandas sin distinguir el canal
    """ 
    data=data.drop(["Channels"],axis=1,inplace=False)
    bandas=data["Bands"].unique()

    fig, ax = plt.subplots(1,1)
    fig.set_size_inches(len(bandas)*2,10)
    sns.violinplot(x='Bands',y="Powers",data=data)
    ax.set_title('Bands powers')
    if plot:
        plt.show()
    return fig 

# ESTUDIOS 

def compare_1S_nB_0C_power(data,name_study,plot=False):
    """
    todos sujetos -1 estudio-todas las bandas sin distinguir el canal
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
            fig, ax = plt.subplots()
            filter= filter_nS_1B_1C_power(data,band,name_channel) 
            sns.violinplot(x='Study',y="Powers",data=filter,ax=axs[col],scale_hue=True,scale='width')
            axs[col].set_title(band+' '+name_channel)
        plt.tight_layout(pad=0.4, w_pad=0.0001, h_pad=0.8)
        if plot:
            plt.show()
    
    else: 
        #sin distinguir el canal
        for band in zip(range(cols),bandas):
            fig, ax = plt.subplots()
            filter= filter_nS_nB_0C_power(data,band)
            sns.violinplot(x='Study',y="Powers",data=filter,ax=axs)
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
    plt.title(name_study +' '+name_group)
    if plot:
        plt.show()
    return fig 
def filter_nS_nG_1B(superdata,group_dict,name_band):
    """
    group_dict={
        'BIOMARCADORES':[CTR,DCL],
        'SRM':['SRM'] # assume datasets with no groups have Group=Study
    }
    
    """
    fil=superdata[superdata["Bands"]==name_band]
    list_df=[]

    for dataset,group_list in group_dict.items():
        for group in group_list:
            auxfil = fil[fil['Group']==group]
            list_df.append(auxfil)
    df=pd.concat((list_df))
    return df

def compare_nS_nG_nB(data,dict_info):
    figures=[]
    bands=data['Bands'].unique()
    for j,band in enumerate(bands):
        fig, ax = plt.subplots()
        filter_group=filter_nS_nG_1B(data,dict_info,band)
        #filter_group['Group']=filter_group['Study']+'-'+filter_group['Group']
        ax=sns.violinplot(x='Group',y="Powers",data=filter_group,ax=ax,hue='Study')
        #ax.get_legend().remove()
        plt.title(band,fontsize=40) 
        plt.xticks(fontsize=40)
        plt.yticks(fontsize=40)   
        fig.set_size_inches(15, 15) 
        figures.append(fig)
    createCollage(figures,800,3)      
    return 

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

def compare_1S_nV_nB(data,name_study): 
    bands=data['Bands'].unique()
    figures=[]
    for num,band in enumerate(bands):
        fig, ax = plt.subplots()
        filter_group=filter_1S_1V_1B(data,name_study,band)
        ax=sns.violinplot(x='Session',y="Powers",data=filter_group,ax=ax)
        plt.title(band,fontsize=40)
        plt.xticks(fontsize=40)
        plt.yticks(fontsize=40)
        fig.set_size_inches(15, 15) 
        figures.append(fig)
    createCollage(figures,800,3)    
    return   


# TOTAL
#compare_nD(datosPowers,plot=True)

# 1 estudio
St=['CHBMP','BIOMARCADORES','SRM']
#St=['BIOMARCADORES']
bands_1 = ['delta','theta','alpha-1','alpha-2','alpha','beta','gamma']
GB = ['G1','G2','CTR','DCL','DTA']
Vs = ['V0','V1','V2','V3','V4']
for Study in St:
    compare_1S_nB_0C_power(datosPowers,Study,plot=True)
    compare_1S_nV_nB(datosPowers,Study)
    for V in Vs:
        compare_1S_1G_nB_0C_power(datosPowers,Study,gr,plot=True)
        compare_1S_1V_nB(datosPowers,Study,V,True)            
    for band in bands_1:
        compare_1S_1B_nC_power(datosPowers,Study,band,plot=True)

#n estudios 
#NOTA: ORGANIZAR PARA QUE SALGAN POR ROWS Y COLS PREGUNTAR
channels = ['FP1', 'FPZ', 'FP2', 'AF3', 'AF4', 'F7', 'F5', 'F3', 'F1', 'FZ', 'F2', 'F4', 'F6', 'F8', 'FC5', 'FC3', 'FC1', 'FCZ', 'FC2', 'FC4', 'FC6', 'T7', 'C5', 'C3', 'C1', 'CZ', 'C2', 'C4', 'C6', 'T8', 'TP7', 'CP5', 'CP3', 'CP1', 'CPZ', 'CP2', 'CP4', 'CP6', 'TP8', 'P7', 'P5', 'P3', 'P1', 'PZ', 'P2', 'P4', 'P6', 'P8', 'PO7', 'PO5', 'PO3', 'POZ', 'PO4', 'PO6', 'PO8', 'O1', 'OZ', 'O2']
for channel in channels:
    compare_nS_nB_power(datosPowers,name_channel=channel,plot=True)
compare_nS_nB_power(datosPowers,name_channel="None",plot=True)

# 1  grupo
for G in GB:
    compare_1S_1G_nB_0C_power(datosPowers,'BIOMARCADORES',G,plot=True)
# n grupos 
info={
   'SRM':['SRM'],
   'BIOMARCADORES':['G1','G2','CTR','DCL','DTA'],
   'CHBMP':['CHBMP']
}
compare_nS_nG_nB(datosPowers,info)

# 1 sessions
#compare_1S_1V_nB(datosPowers,'BIOMARCADORES','G1',True)
# n sessions 
#compare_1S_nV_nB(datosPowers,'BIOMARCADORES')
