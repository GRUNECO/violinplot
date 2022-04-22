from Graphics.graphicsViolin import get_dataframe_prep

import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
from datasets import BIOMARCADORES,SRM,BIOMARCADORES_test,SRM_test
from Graphics.graphicsViolin import get_dataframe_prep,createCollage,filter_nS_nG_1M
import numpy as np
import itertools
from pprint import pprint


Studies=[BIOMARCADORES,SRM]
Studies_test=[BIOMARCADORES_test,SRM_test]
dataPrepOriginal,dataPrepBefore,dataPrepAfter=get_dataframe_prep(Studies)

#PREP ESTUDIO 
def compare_1S_nM_prep(data,name_study,title):
    s=data["Study"]==name_study
    filter=data[s]
    filter_study=data.drop(["Study","Group","Session","Subject"],axis=1,inplace=False)
    metrics=filter_study.keys()
    figures=[]
    for i,metric in enumerate(metrics):
        fig,ax=plt.subplots(figsize=(10,5))
        ax=sns.violinplot(y=metric,x="Study",data= filter,fontsize=70,ax=ax)
        plt.title(metric +' '+ title,fontsize=30)
        plt.xticks(fontsize=30)
        plt.yticks(fontsize=30)
        figures.append(fig)

    plt.tight_layout()
    createCollage(figures,3000,3) 

def compare_nS_nM_prep(data,title):
    filter_study=data.drop(["Study","Group","Session","Subject"],axis=1,inplace=False)
    metrics=filter_study.keys()
    figures=[]
    for i,metric in enumerate(metrics):
        fig,ax=plt.subplots(figsize=(10,5))
        ax=sns.violinplot(y=metric,x="Study",data= data,fontsize=70,ax=ax)
        plt.title(metric+' '+title,fontsize=15)
        plt.xticks(fontsize=15)
        plt.yticks(fontsize=15)
        figures.append(fig)
    plt.tight_layout()
    createCollage(figures,3000,3) 
    return

# GRUPO

def compare_nS_nG_nB_prep(data,dict_info,title):
    figures_i=[]
    figures_f=[]
    filter_study=data.drop(["Study","Group","Session","Subject"],axis=1,inplace=False)
    metrics=filter_study.keys()
    for i,metric in enumerate(metrics):
        fig, ax = plt.subplots(figsize=(15,10))
        filter_group=filter_nS_nG_1M(data,dict_info)
        ax=sns.violinplot(x='Group',y=metric,data=filter_group,ax=ax,hue='Study')
        plt.title(metric +' '+title,fontsize=35)
        plt.xticks(fontsize=35)
        plt.yticks(fontsize=35)   
        figures_i.append(fig)
    createCollage(figures_i,3000,3)       
    return 

# VISITA
def compare_1S_nV_nM_prep(data,name_study,title):
    filter_metrics=data.drop(["Study","Group","Session","Subject"],axis=1,inplace=False)
    metrics=filter_metrics.keys() 
    figures=[]
    for i,metric in enumerate(metrics):
        fig, ax = plt.subplots(figsize=(15,10))
        filt_study=data["Study"]==name_study
        filter=data[filt_study]
        ax=sns.violinplot(x='Session',y=metric,data=filter,ax=ax,hue='Study')
        plt.title(metric +' '+ title,fontsize=40)
        plt.xticks(fontsize=40)
        plt.yticks(fontsize=40) 
        figures.append(fig)

    createCollage(figures,3000,3)    
    return



'''
# 1 estudio
compare_1S_nM_prep(dataPrepOriginal,'BIOMARCADORES','ORIGINAL')
compare_1S_nM_prep(dataPrepBefore,'BIOMARCADORES','BEFORE')
compare_1S_nM_prep(dataPrepAfter,'BIOMARCADORES','AFTER')

# n estudios 
compare_nS_nM_prep(dataPrepOriginal,'ORIGINAL')
compare_nS_nM_prep(dataPrepBefore,'BEFORE')
compare_nS_nM_prep(dataPrepAfter,'AFTER')

#n grupos
group_dict={
    'BIOMARCADORES':['CTR','G1','G2','DCL'],
    'SRM':['SRM']
}


group_dict2={
    'BIOMARCADORES':['CTR','G1','G2','DCL']
}
compare_nS_nG_nB_prep(dataPrepOriginal,group_dict,'ORIGINAL')
compare_nS_nG_nB_prep(dataPrepBefore,group_dict,'BEFORE')
compare_nS_nG_nB_prep(dataPrepAfter,group_dict,'AFTER')
compare_nS_nG_nB_prep(dataPrepOriginal,group_dict2,'ORIGINAL')
compare_nS_nG_nB_prep(dataPrepBefore,group_dict2,'BEFORE')
compare_nS_nG_nB_prep(dataPrepAfter,group_dict2,'AFTER')

# n visitas 
compare_1S_nV_nM_prep(dataPrepOriginal,'BIOMARCADORES','ORIGINAL')
compare_1S_nV_nM_prep(dataPrepBefore,'BIOMARCADORES','BEFORE')
compare_1S_nV_nM_prep(dataPrepAfter,'BIOMARCADORES','AFTER')
'''