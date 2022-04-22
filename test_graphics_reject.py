import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
from datasets import BIOMARCADORES,SRM,BIOMARCADORES_test,SRM_test
from Graphics.graphicsViolin import get_dataframe_reject,create_collage,createCollage
import numpy as np
from pprint import pprint

Studies=[BIOMARCADORES,SRM]
Studies_test=[BIOMARCADORES_test,SRM_test]

datosReject=get_dataframe_reject(Studies)

# ESTUDIO 

def compare_1S_0C_nM_reject(data,name_study):
    """
    todos sujetos, 1 estudio todas las bandas sin distinguir el canal
    """ 
    s=data["Study"]==name_study
    filter=data[s]
    filter_study=data.drop(["Study","Group","Session","Subject"],axis=1,inplace=False)
    metrics=filter_study.keys()
    figures_i=[]
    for i,metric in enumerate(metrics[0:5]):
        fig,ax=plt.subplots(figsize=(10,5))
        ax=sns.violinplot(y=metric,x="Study",data= filter,fontsize=70,ax=ax)
        plt.title(metric,fontsize=15)
        plt.xticks(fontsize=15)
        plt.yticks(fontsize=15)
        figures_i.append(fig)

    plt.tight_layout()
    figures_f=[]
    for i,metric in enumerate(metrics[5:]):
        fig,ax=plt.subplots(figsize=(15,10))
        ax=sns.violinplot(y=metric,x="Study",data= filter,fontsize=70,ax=ax)
        plt.title(metric,fontsize=35)
        plt.xticks(fontsize=35)
        plt.yticks(fontsize=35)
        figures_f.append(fig)
    plt.tight_layout()
    createCollage(figures_i,3000,3) 
    createCollage(figures_f,3000,4) 
    return 

def compare_nS_0C_nM_reject(data):
    """
    todos sujetos, 1 estudio todas las bandas sin distinguir el canal
    """ 
    filter_study=data.drop(["Study","Group","Session","Subject"],axis=1,inplace=False)
    metrics=filter_study.keys()
    figures_i=[]
    for i,metric in enumerate(metrics[0:5]):
        fig,ax=plt.subplots(figsize=(10,5))
        ax=sns.violinplot(y=metric,x="Study",data= data,fontsize=70,ax=ax)
        plt.title(metric,fontsize=15)
        plt.xticks(fontsize=15)
        plt.yticks(fontsize=15)
        figures_i.append(fig)

    plt.tight_layout()
    figures_f=[]
    for i,metric in enumerate(metrics[5:]):
        fig,ax=plt.subplots(figsize=(15,10))
        ax=sns.violinplot(y=metric,x="Study",data= data,fontsize=70,ax=ax)
        plt.title(metric,fontsize=35)
        plt.xticks(fontsize=35)
        plt.yticks(fontsize=35)
        figures_f.append(fig)
    plt.tight_layout()
    createCollage(figures_i,3000,3) 
    createCollage(figures_f,3000,4) 
    return 

# GRUPO
def filter_nS_nG_1M_reject(superdata,group_dict):
    """
    group_dict={
        'BIOMARCADORES':[CTR,DCL],
        'SRM':['SRM'] # assume datasets with no groups have Group=Study
    }
    
    """
    fil=superdata
    list_df=[]

    for dataset,group_list in group_dict.items():
        for group in group_list:
            auxfil = fil[fil['Group']==group]
            list_df.append(auxfil)
    df=pd.concat((list_df))
    return df

def compare_nS_nG_nB_reject(data,dict_info):
    figures_i=[]
    figures_f=[]
    filter_study=data.drop(["Study","Group","Session","Subject"],axis=1,inplace=False)
    metrics=filter_study.keys()
    for i,metric in enumerate(metrics[0:5]):
        fig, ax = plt.subplots(figsize=(15,10))
        filter_group=filter_nS_nG_1M_reject(data,dict_info)
        #filter_group['Group']=filter_group['Study']+'-'+filter_group['Group']
        ax=sns.violinplot(x='Group',y=metric,data=filter_group,ax=ax,hue='Study')
        #ax.get_legend().remove()
        plt.title(metric,fontsize=35)
        plt.xticks(fontsize=35)
        plt.yticks(fontsize=35)   
        figures_i.append(fig)
    for i,metric in enumerate(metrics[5:]):
        fig, ax = plt.subplots(figsize=(15,10))
        filter_group=filter_nS_nG_1M_reject(data,dict_info)
        #filter_group['Group']=filter_group['Study']+'-'+filter_group['Group']
        ax=sns.violinplot(x='Group',y=metric,data=filter_group,ax=ax,hue='Study')
        #ax.get_legend().remove()
        plt.title(metric,fontsize=35) 
        plt.xticks(fontsize=35)
        plt.yticks(fontsize=35)  
        figures_f.append(fig)
    createCollage(figures_i,3000,3) 
    createCollage(figures_f,3000,4)       
    return 

# VISITAS
    
def compare_1S_nV_nM_reject(data,name_study):
    filter_metrics=data.drop(["Study","Group","Session","Subject"],axis=1,inplace=False)
    metrics=filter_metrics.keys() 
    figures_i=[]
    figures_f=[]
    for i,metric in enumerate(metrics[0:5]):
        fig, ax = plt.subplots(figsize=(15,10))
        filt_study=data["Study"]==name_study
        filter=data[filt_study]
        ax=sns.violinplot(x='Session',y=metric,data=filter,ax=ax)
        plt.title(metric,fontsize=40)
        plt.xticks(fontsize=40)
        plt.yticks(fontsize=40) 
        figures_i.append(fig)

    for i,metric in enumerate(metrics[5:]):
        fig, ax = plt.subplots(figsize=(15,10))
        filt_study=data["Study"]==name_study
        filter=data[filt_study]
        ax=sns.violinplot(x='Session',y=metric,data=filter,ax=ax)
        plt.title(metric,fontsize=40)
        plt.xticks(fontsize=40)
        plt.yticks(fontsize=40) 
        figures_f.append(fig)
    createCollage(figures_i,3000,3) 
    createCollage(figures_f,3000,4)     
    return   

'''
# 1 estudio
compare_1S_0C_reject(datosReject,'BIOMARCADORES') 
#  n estudios 
compare_nS_0C_nM_reject(datosReject)
# n group 
group_dict={
    'BIOMARCADORES':['CTR','G1','G2','DCL'],
    'SRM':['SRM'] # assume datasets with no groups have Group=Study
}
compare_nS_nG_nB_reject(datosReject,group_dict)
#n visit
compare_1S_nV_nM_reject(datosReject,'BIOMARCADORES') 
'''
