import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
from datasets import BIOMARCADORES,SRM,BIOMARCADORES_test,SRM_test
from Graphics.graphicsViolin import get_dataframe_wica,createCollage
import numpy as np
import itertools
from pprint import pprint


Studies=[BIOMARCADORES,SRM]
Studies_test=[BIOMARCADORES_test,SRM_test]
datosWica=get_dataframe_wica(Studies)

#TOTAL
def compare_nD_wica(data,plot=False):
    figure1=plt.figure(figsize=(30,60), dpi=30)
    sns.violinplot(y='Components',data=data)
    plt.xticks(fontsize=40)
    plt.yticks(fontsize=40)
    figure1.tight_layout()
    if plot:
        plt.show()
    return figure1

compare_nD_wica(datosWica,True)
# ESTUDIO

def compare_1S_wica(data,name_study,plot=False):
    s=data["Study"]==name_study
    filter_study=data[s]
    figure1=plt.figure(figsize=(30,60), dpi=30)
    sns.violinplot(x='Study',y='Components',data=filter_study)
    plt.xticks(fontsize=70)
    plt.yticks(fontsize=70)
    figure1.tight_layout()
    if plot:
        plt.show()
    return figure1

def compare_nS_wica(data):
    fig,ax=plt.subplots(figsize=(10,5))
    sns.violinplot(x='Study',y='Components',data=data)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.show()
    return 
# WICA  VISITAS
def compare_1S_nV_wica(data,name_study):
    s=data["Study"]==name_study
    filter_study=data[s]
    fig,ax=plt.subplots(figsize=(10,5))
    sns.violinplot(x='Session',y='Components',data=filter_study)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.show()
    return 

# GRUPOS
def filter_nS_nG_1B(superdata,group_dict):
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

def compare_nS_nG_wica(data,dict_info):
    fig, ax = plt.subplots(figsize=(15,10))
    filter_group=filter_nS_nG_1B(data,dict_info)
    ax=sns.violinplot(x='Group',y="Components",data=filter_group,ax=ax,hue='Study')
    plt.xticks(fontsize=40)
    plt.yticks(fontsize=40)
    plt.show()        
    return 


'''
#TOTAL

# 1 estudio
compare_1S_wica(datosWica,'SRM',True)
# n estudios 
compare_nS_wica(datosWica)
# n grupos

# n visitas
compare_1S_nV_wica(datosWica,'BIOMARCADORES')


#N GRUPOS
group_dict1={
    'BIOMARCADORES':['CTR','DCL','G1','G2'],
    'SRM':['SRM'] # assume datasets with no groups have Group=Study
}
compare_nS_nG_wica(datosWica,group_dict1)

group_dict2={
    'BIOMARCADORES':['CTR','DCL','G1','G2'],
}
compare_nS_nG_wica(datosWica,group_dict2)
'''